# urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/create_team/', views.createTeam, name='create_team'),
    path('list_competitions/', views.list_competitions, name='list_competitions'),
    path('<int:id>', views.showComp, name='ShowComp'),
    path('<int:id>/join_team/', views.joinTeam, name='join_team'),
    path('leave/', views.leave, name='leave')

    # Add other URLs as needed
]
