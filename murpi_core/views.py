from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseServerError
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.messages import (debug, info, success, warning, error)
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Count, ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from MURPI.settings import DEFAULT_AVATAR, DEFAULT_BACKGROUND
from .utils.helpers import dict_has_keys, delete_uploaded_file
from .models import Player, Universe, World, Place, Roleplay, Scene, RoleplayPost
from .forms import PlaceForm, WorldForm, UniverseForm, RoleplayForm


@require_http_methods(['GET', 'POST', 'HEAD'])
def register(request):
    if request.method in ['GET', 'HEAD']:
        if request.user.is_authenticated():
            try:
                player = request.user.player
                return redirect(reverse('player', kwargs={'username': player.user.username}))
            except Exception:
                return HttpResponseServerError("<h1>Your user is not associated with a player!</h1>")
        else:
            return render(request, 'murpi_core/register.html')
    elif request.method == 'POST':
        try:
            if dict_has_keys(request.POST, ('username', 'email', 'password',), check_not_empty=True):
                User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                new_user = User.objects.get(username=request.POST['username'])
                Player.objects.create(avatar=DEFAULT_AVATAR, user=new_user)
                success(request, "You successfully created a player! Now please login.")
                return redirect(reverse("login"))
            else:
                error(request, 'Username, email or password cannot be empty')
                return redirect(reverse("register"))
        except IntegrityError:
            error(request, 'Username ' + request.POST['username'] + ' is taken.')
            return redirect(reverse("register"))
    else:
        raise Http404('Only GET, POST, and HEAD HTTP methods allowed.')


@require_http_methods(['GET', 'POST', 'HEAD'])
def login(request):
    if request.method in ['GET', 'HEAD']:
        if request.user.is_authenticated():
            try:
                player = Player.objects.get(user=request.user)
                return redirect(reverse('player', kwargs={'username': player.user.username}))
            except Exception:
                return HttpResponseServerError("<h1>Your user is not associated with a player!</h1>")
        else:
            return render(request, 'murpi_core/login.html')
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
        raise Http404('Only GET, POST, and HEAD HTTP methods allowed.')


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
def create_universe(request):
    if request.method in ['GET', 'HEAD']:
        return render(request, "murpi_core/create_universe.html", {'form': UniverseForm()})
    elif request.method == 'POST':
        form = UniverseForm(request.POST, request.FILES)
        if form.is_valid():
            universe = form.save(commit=False)
            universe.owner = Player.objects.get(user__username=request.user.username)
            universe.save()
            return redirect(reverse('universe', kwargs={'universe_id': universe.id}))
        else:
            return render(request, "murpi_core/create_universe.html", {'form': form})
    else:
        raise Http404('Only GET, POST, and HEAD HTTP methods allowed.')


@require_safe
def retrieve_universe(request, universe_id):
    universe = Universe.objects.get(pk=universe_id)
    return render(request, "murpi_core/universe.html", {'universe': universe})


@require_http_methods(['GET', 'POST', 'HEAD'])
def create_world(request, universe_id):
    universe = get_object_or_404(Universe, pk=universe_id)
    context_dict = {'universe_id': universe_id}
    if request.method in ['GET', 'HEAD']:
        context_dict['form'] = WorldForm()
        return render(request, "murpi_core/create_world.html", context_dict)
    elif request.method == 'POST':
        form = WorldForm(request.POST, request.FILES)
        if form.is_valid():
            world = form.save(commit=False)
            world.owner = Player.objects.get(user__username=request.user.username)
            world.universe = universe
            try:
                world.save()
            except IntegrityError:
                delete_uploaded_file(World, 'thumbnail', world.thumbnail.name)
                form.add_error('name', 'This world already exists in the current universe.')
                context_dict['form'] = form
                return render(request, "murpi_core/create_world.html", context_dict)
            return redirect(reverse('world', kwargs={'world_id': world.id}))
        else:
            context_dict['form'] = form
            return render(request, "murpi_core/create_world.html", context_dict)
    else:
        raise Http404('Only GET, POST, and HEAD HTTP methods allowed.')


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
            place = form.save(commit=False)
            place.owner = Player.objects.get(user__username=request.user.username)
            place.world = world
            try:
                place.save()
            except IntegrityError:
                delete_uploaded_file(Place, 'thumbnail', place.thumbnail.name)
                form.add_error('name', 'This place already exists in the current world.')
                context_dict['form'] = form
                return render(request, "murpi_core/create_place.html", context_dict)
            return redirect(reverse('place', kwargs={'place_id': place.id}))
        else:
            context_dict['form'] = form
            return render(request, "murpi_core/create_place.html", context_dict)
    else:
        raise Http404('Only GET, POST, and HEAD HTTP methods allowed.')


@require_safe
def retrieve_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return render(request, "murpi_core/place.html", {'place': place})


@require_safe
def retrieve_universes(request):
    universes = Universe.objects.all()\
        .order_by('date_modified')\
        .annotate(num_rps=Count('world__place__scene__roleplay', distinct=True))
    paginator = Paginator(universes, 10)
    page = request.GET.get('page')
    try:
        u_sub = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        u_sub = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        u_sub = paginator.page(paginator.num_pages)
    return render(request, "murpi_core/universes.html", {'universes': u_sub})


@require_safe
def retrieve_worlds(request, universe_id):
    universe = get_object_or_404(Universe, pk=universe_id)
    worlds = World.objects.all()\
        .filter(universe_id=universe_id)\
        .order_by('date_modified')\
        .annotate(num_posts=Count('place__scene__roleplaypost'))
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


@require_safe
def retrieve_places(request, world_id):
    world = get_object_or_404(World, pk=world_id)
    places = Place.objects.all()\
        .filter(world_id=world_id)\
        .order_by('date_modified')\
        .annotate(num_posts=Count('scene__roleplaypost'))
    paginator = Paginator(places, 10)
    page = request.GET.get('page')
    try:
        places_sub = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        places_sub = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        places_sub = paginator.page(paginator.num_pages)
    return render(request, "murpi_core/places.html", {'world': world, 'places': places_sub})


@require_safe
def retrieve_players(request):
    if request.GET.get('q'):
        players = Player.objects\
            .filter(user__username__contains=request.GET.get('q'))\
            .annotate(num_posts=Count('rp_post_author'))\
            .order_by('id')
    else:
        players = Player.objects.all()\
            .annotate(num_posts=Count('rp_post_author'))\
            .order_by('id')
    return render(request, "murpi_core/players.html", {'players': players})


@require_http_methods(['GET', 'POST', 'HEAD'])
def create_rp(request):
    if request.method in ['GET', 'HEAD']:
        return render(request, "murpi_core/create_rp.html", {'form': RoleplayForm()})
    elif request.method == 'POST':
        form = RoleplayForm(request.POST, request.FILES)
        if form.is_valid():
            rp = form.save(commit=False)
            rp.game_master = Player.objects.get(user__username=request.user.username)
            rp.save()
            return redirect(reverse('rp', kwargs={'rp_id': rp.id}))
        else:
            print form.errors
            return render(request, "murpi_core/create_rp.html", {'form': form})
    else:
        raise Http404('Only GET, POST, and HEAD HTTP methods allowed.')


@require_safe
def retrieve_rp(request, rp_id):
    rp = get_object_or_404(Roleplay, pk=rp_id)
    try:
        most_recent_post_time = RoleplayPost.objects.filter(scene__roleplay_id=rp_id)\
            .order_by('date_created').latest('date_created').date_created
    except ObjectDoesNotExist:
        most_recent_post_time = None
    return render(request, "murpi_core/rp.html", {'rp': rp, 'most_recent_post_time': most_recent_post_time})