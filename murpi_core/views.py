from django.views.decorators.http import require_safe, require_POST
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect
from utilities.helpers import dict_has_keys
from django.contrib.auth.models import User
from .models import Player


@require_safe()
def retrieve_player(request, player_name):
    player = get_object_or_404(Player, name=player_name)
    return render(request, "player.html", {'player': player})


@require_POST()
def create_player(request):
    if dict_has_keys(request.POST, ('username', 'email', 'password'), check_not_empty=True):
        new_user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        new_player = Player(photo=Player.retrieve_default_avatar(), user=new_user)
        return redirect(reverse("core:home"), player={'player': new_player})
    else:
        return render(request, "player_create.html", {'error': 'Username, email or password cannot be empty.'})


@require_POST()
def login(request):
    if dict_has_keys(request.POST, ('username', 'password'), check_not_empty=True):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                player = Player.objects.get(user=user)
                if player is not None:
                    return redirect(reverse("core:home"), player={'player': player})
                else:
                    render(request, "login.html", {'error': 'This login is not associated with a user. '
                                                            'Please contact an administrator.'})
            else:
                render(request, "login.html", {'error': 'That account is disabled!'})
        else:
            # the authentication system was unable to verify the username and password
            render(request, "login.html", {'error': 'That username or password is incorrect.'})