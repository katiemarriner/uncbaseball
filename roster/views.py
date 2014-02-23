from django.shortcuts import render
from roster.models import Player

# Create your views here.
def home(request):
    context = {
        'player_count': Player.objects.count(),
    }
    return render(request, "base.html", context)

def player(request, pk):
    student = get_object_or_404(Student, id=pk)
    return render(request, "roster/player.html", {'player': player})

def playerList(request):
    player_list = Player.objects.all()
    return render(request, 'roster/player_list.html', {"players": players})