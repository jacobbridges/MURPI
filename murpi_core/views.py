from django.http import Http404
from django.shortcuts import render
from .models import Player


def player_details(request, player_id):
    try:
        player = Player.objects.get(pk=player_id)
    except Player.DoesNotExist:
        raise Http404("Player does not exist")
    return render(request, "player.html", {'player': player})