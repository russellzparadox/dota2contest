from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.timezone import now

from competitions.models import Competitions, Teams


# Create your views here.
@login_required
def createTeam(request, id):
    competition = Competitions.objects.get(id=id)

    if request.method == 'POST':
        team_name = request.POST['team_name']
        user = request.user

        team = Teams.objects.create(
            Name=team_name,
            creator=user,
            competition=competition,
        )

        team.members.add(user)  # Add the creator as a member
        return redirect('ShowComp', id=id)

    return render(request, 'create_team.html', {'competition': competition})


@login_required
def list_competitions(request):
    # user = request.user
    coms = Competitions.objects.filter(end_date__gt=now()).filter(start_date__lte=now())
    return render(request, 'competitionList.html', {'comps': coms})


def showComp(request, id):
    user = request.user
    competition = Competitions.objects.get(id=id)
    teams_in_competition = Teams.objects.filter(competition=competition)
    count = 0
    for team in teams_in_competition:
        count = count + team.members.count()
    number_of_teams = teams_in_competition.count()
    user_has_team = user.has_team(competition)
    user_team = Teams.objects.filter(members=user, competition=competition).first()
    context = {
        'competition': competition,
        'teams_in_competition': teams_in_competition,
        'user_has_team': user_has_team,
        'user': user,
        'user_team': user_team,
        'count': count
    }

    return render(request, 'competetion_info.html', context)


@login_required
def joinTeam(request, id):
    competition = Competitions.objects.get(id=id)

    if request.method == 'POST':
        user = request.user
        if request.POST['flag'] == '1':
            team = int(request.POST['team_name'])
            team = Teams.objects.get(id=team)
            if team.members.count() <= 5:
                team.members.add(user)
                return redirect('ShowComp', id=id)
        team_name = request.POST['search']
        user = request.user

        try:
            teams = Teams.objects.filter(Name__icontains=team_name, competition=competition)
            return render(request, 'join_team.html', {'competition': competition, 'teams': teams})
            # if team.members.count() < 5:
            #     team.members.add(user)
        except Teams.DoesNotExist:
            pass

        return redirect('ShowComp', id=id)

    return render(request, 'join_team.html', {'competition': competition})


@login_required
def leave(request):
    if request.method == 'POST':
        id = request.POST['teamid']
        team = Teams.objects.get(id=id)
        team.remove_member(request.user)
        return redirect(request.META.get('HTTP_REFERER', '/default-url/'))
