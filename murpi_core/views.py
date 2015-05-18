from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.defaults import page_not_found
from django.contrib.messages import (debug, info, success, warning, error)
from django.contrib.auth.models import User
from django.db import IntegrityError

from .utils.helpers import dict_has_keys
from .models import Player, Photo


@require_safe
def retrieve_player(request, username):
    user = get_object_or_404(User, username=username)
    player = get_object_or_404(Player, user=user)
    return render(request, "murpi_core/player.html", {'player': player})


@require_safe
def retrieve_player_characters(request, username):
    players = Player.objects.filter(user__username=username)
    if len(players) == 1:
        return render(request, "murpi_core/characters.html", {'player': players[0]})
    else:
        return page_not_found(request)


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