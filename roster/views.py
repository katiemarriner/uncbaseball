from django.shortcuts import render
from roster.models import Player

# Create your views here.
def home(request):
    context = {
        'player_count': Player.objects.count(),
    }
    return render(request, "base.html", context)

def player(request, pk):
    player = get_object_or_404(Player, id=pk)
    return render(request, "roster/player.html", {'player': player})

def playerList(request):
    player_list = Player.objects.all()
    return render(request, 'roster/player_list.html', {"players": players})

def staff(request, pk):
    staff = get_object_or_404(Staff, id=pk)
    return render(request, "roster/staff.html", {"staff": staff})

def staffList(request):
    staff_list = Staff.object.all()
    return render(request, 'roster/staff_list.html', {"staff": staff})