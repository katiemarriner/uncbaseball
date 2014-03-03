from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from roster.models import Player, Coach

# Create your views here.
def home(request):
    context = {
        'player_count': Player.objects.count(),
    }
    return render(request, "roster/home.html", context)

def player(request, pk):
    player = get_object_or_404(Player, id=pk)
    return render(request, "roster/player.html", {'player': player})

def playerList(request):
    player_list = Player.objects.all()
    return render(request, 'roster/player_list.html', {'players': player_list})

def coach(request, pk):
    coach = get_object_or_404(Coach, id=pk)
    return render(request, "roster/coach.html", {'coach': coach})

def coachList(request):
    coach_list = Coach.objects.all()
    return render(request, 'roster/coach_list.html', {'coaches': coach_list})