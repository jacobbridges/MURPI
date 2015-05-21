from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.defaults import page_not_found
from django.contrib.messages import (debug, info, success, warning, error)
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .utils.helpers import dict_has_keys
from .models import Player, Photo, Universe, World, Place
from .forms import PlaceForm


@require_http_methods(['GET', 'POST', 'HEAD'])
def register(request):
    if request.method in ['GET', 'HEAD']:
        if request.user.is_authenticated() and request.user.player:
            return redirect(reverse('player', kwargs={'username': request.user.username}))
        else:
            return render(request, 'murpi_core/register.html')
    elif request.method == 'POST':
        try:
            if dict_has_keys(request.POST, ('username', 'email', 'password',), check_not_empty=True):
                User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                new_user = User.objects.get(username=request.POST['username'])
                default_avatar = Photo.objects.get(file_name='img/avatar/default.png')
                Player.objects.create(avatar=default_avatar, user=new_user)
                success(request, "You successfully created a player! Now please login.")
                return redirect(reverse("login"))
            else:
                error(request, 'Username, email or password cannot be empty')
                return redirect(reverse("register"))
        except IntegrityError:
            error(request, 'Username ' + request.POST['username'] + ' is taken.')
            return redirect(reverse("register"))
    else:
        return page_not_found(request)


@require_http_methods(['GET', 'POST', 'HEAD'])
def login(request):
    if request.method in ['GET', 'HEAD']:
        if request.user.is_authenticated() and request.user.player:
            return redirect(reverse('player', kwargs={'username': request.user.username}))
        else:
            return render(request, "murpi_core/login.html")
    elif request.method == 'POST':
        if dict_has_keys(request.POST, ('username', 'password'), check_not_empty=True):
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    if user.player:
                        django_login(request, user)
                        return redirect(reverse("player", kwargs={"username": user.username}))
                    else:
                        error(request, 'Your user account is broken! Please contact an admin.')
                        return redirect(reverse("login"))
                else:
                    error(request, 'Your account is disabled!')
                    return redirect(reverse("login"))
            else:
                request.session['username'] = request.POST['username']
                error(request, 'Incorrect username or password.')
                return redirect(reverse("login"))
        else:
            request.session['username'] = request.POST['username']
            error(request, 'Username or password cannot be empty')
            return redirect(reverse("login"))
    else:
        return page_not_found(request)


@require_safe
def logout(request):
    django_logout(request)
    return redirect(reverse('login'))


@require_safe
def retrieve_player(request, username):
    player = get_object_or_404(Player, user__username=username)
    return render(request, "murpi_core/player.html", {'player': player})


@require_safe
def retrieve_player_characters(request, username):
    player = get_object_or_404(Player, user__username=username)
    return render(request, "murpi_core/characters.html", {'player': player})


@require_http_methods(['GET', 'POST', 'HEAD'])
# FOR SOME REASON NOT WORKING WITH POST..
def create_world(request, universe_id):
    universe = get_object_or_404(Universe, pk=universe_id)
    context_dict = {'universe_id': universe_id}
    if request.method in ['GET', 'HEAD']:
        return render(request, "murpi_core/create_world.html", context_dict)
    elif request.method == 'POST':
        # TODO: Convert to Django form for more validation
        if dict_has_keys(request.POST, ('name', 'is_public', 'description')) and \
           'thumbnail' in request.FILES and 'background' in request.FILES:
            author = Player.objects.get(user__username=request.user.username)
            thumbnail = Photo(file_name=request.FILES['thumbnail'])
            thumbnail.save()
            background = Photo(file_name=request.FILES['background'])
            background.save()
            world = World.objects.create(owner=author, name=request.POST['name'], universe=universe,
                                         description=request.POST['description'],
                                         is_public=True if request.POST['is_public'] == 'on' else False,
                                         thumbnail=thumbnail, background=background)
            return redirect(reverse('world', kwargs={'world_id': world.id}))
        else:
            return page_not_found(request)
    else:
        return page_not_found(request)


@require_safe
def retrieve_world(request, world_id):
    world = get_object_or_404(World, pk=world_id)
    return render(request, "murpi_core/world.html", {'world': world})


@require_http_methods(['GET', 'POST', 'HEAD'])
def create_place(request, world_id):
    world = get_object_or_404(World, pk=world_id)
    context_dict = {'world_id': world_id}
    if request.method in ['GET', 'HEAD']:
        context_dict['form'] = PlaceForm()
        return render(request, "murpi_core/create_place.html", context_dict)
    elif request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            author = Player.objects.get(user__username=request.user.username)
            thumbnail = Photo(file_name=form.cleaned_data['thumbnail'])
            thumbnail.save()
            place = Place.objects.create(owner=author, name=form.cleaned_data['name'], world=world,
                                         description=form.cleaned_data['description'],
                                         is_public=form.cleaned_data['is_public'], thumbnail=thumbnail)
            return redirect(reverse('place', kwargs={'place_id': place.id}))
        else:
            context_dict['form'] = form
            return render(request, "murpi_core/create_place.html", context_dict)
    else:
        return page_not_found(request)


@require_safe
def retrieve_place(request, place_id):
    place = get_object_or_404(Player, pk=place_id)
    return render(request, "murpi_core/place.html", {'place': place})


@require_safe
def retrieve_worlds(request, universe_id):
    universe = get_object_or_404(Universe, pk=universe_id)
    worlds = World.objects.all().filter(universe_id=universe_id)
    paginator = Paginator(worlds, 10)
    page = request.GET.get('page')
    try:
        worlds_sub = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        worlds_sub = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        worlds_sub = paginator.page(paginator.num_pages)
    return render(request, "murpi_core/worlds.html", {'universe': universe, 'worlds': worlds_sub})