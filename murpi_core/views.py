from django.views.decorators.http import require_safe, require_POST
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect
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


@require_POST
def create_player(request):
    try:
        if dict_has_keys(request.POST, ('username', 'email', 'password',), check_not_empty=True):
            User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            new_user = User.objects.get(username=request.POST['username'])
            default_avatar = Photo.objects.get(file_name='img/avatar/default.png')
            Player.objects.create(avatar=default_avatar, user=new_user)
            new_player = Player.objects.get(user=new_user)
            return redirect(reverse("player", kwargs={"username": new_player.user.username}))
        else:
            error(request, 'Username, email or password cannot be empty')
            return render(request, "murpi_core/register.html")
    except IntegrityError:
        error(request, 'Username ' + request.POST['username'] + ' is taken.')
        return redirect(reverse("show_register"))


@require_safe
def show_create_player(request):
    if request.user.is_authenticated() and request.user.player:
        return redirect(reverse('player', kwargs={'username': request.user.username}))
    else:
        return render(request, "murpi_core/register.html")


@require_POST
def login(request):
    if dict_has_keys(request.POST, ('username', 'password'), check_not_empty=True):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                if user.player:
                    django_login(request, user)
                    return redirect(reverse("player", kwargs={"username": user.username}))
                else:
                    error(request, 'Your user account is broken! Please contact an admin.')
                    return redirect(reverse("show_login"))
            else:
                error(request, 'Your account is disabled!')
                return redirect(reverse("show_login"))
        else:
            request.session['username'] = request.POST['username']
            error(request, 'Incorrect username or password.')
            return redirect(reverse("show_login"))
    else:
        request.session['username'] = request.POST['username']
        error(request, 'Username or password cannot be empty')
        return redirect(reverse("show_login"))


@require_safe
def show_login(request):
    if request.user.is_authenticated() and request.user.player:
        return redirect(reverse('player', kwargs={'username': request.user.username}))
    else:
        return render(request, "murpi_core/login.html")


@require_safe
def logout(request):
    django_logout(request)
    return redirect(reverse('show_login'))