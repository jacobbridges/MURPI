from django.views.decorators.http import require_safe, require_POST
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError

from .utils.helpers import dict_has_keys
from .models import Player


@require_safe
def retrieve_player(request, username):
    user = get_object_or_404(User, username=username)
    player = get_object_or_404(Player, user=user)
    return render(request, "murpi_core/player.html", {'player': player})


@require_POST
def create_player(request):
    try:
        if dict_has_keys(request.POST, ('username', 'email', 'password',), check_not_empty=True):
            new_user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            new_player = Player(photo=Player.retrieve_default_avatar(), user=new_user)
            return redirect("core:player", username=new_player.user.username)
        else:
            return render(request, "murpi_core/register.html", {'error': 'Username, email or password cannot be empty.'})
    except IntegrityError as ie:
        return render(request, "murpi_core/register.html", {'error': 'Username ' + request.POST['username'] + ' is taken.'})


@require_safe
def show_create_player(request):
    return render(request, "murpi_core/register.html")


@require_POST
def login(request):
    if dict_has_keys(request.POST, ('username', 'password'), check_not_empty=True):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                player = Player.objects.get(user=user)
                if player is not None:
                    return redirect(reverse("core:home"), player={'player': player})
                else:
                    render(request, "murpi_core/login.html", {'error': 'This login is not associated with a user. '
                                                              'Please contact an administrator.'})
            else:
                render(request, "murpi_core/login.html", {'error': 'That account is disabled!'})
        else:
            # the authentication system was unable to verify the username and password
            render(request, "murpi_core/login.html", {'error': 'That username or password is incorrect.'})


@require_safe
def show_login(request):
    return render(request, "murpi_core/login.html")