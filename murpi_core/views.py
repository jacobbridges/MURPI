from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Player


def player_details(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, "player.html", {'player': player})