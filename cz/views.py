from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Player, Team, Event, Eventtournament, Clubs, Tournamenttype, Tournament, Tournamentdraw
from .serializers import (
    PlayerListSerializer, PlayerDetailSerializer, TeamListSerializer, TeamDetailSerializer,
    EventListSerializer, EventDetailSerializer, 
    ClubsListSerializer, ClubsDetailSerializer, TournamenttypeListSerializer, TournamenttypeDetailSerializer,
    TournamentListSerializer, TournamentDetailSerializer, TournamentdrawListSerializer, TournamentdrawDetailSerializer

)


class ClubsModelViewSet(viewsets.ModelViewSet):
    queryset = Clubs.objects.all()
    # serializer_class = ClubsListSerializer  # Default serializer
    lookup_field = 'clubid'

    def get_serializer_class(self):
        if self.action == 'list':
            return ClubsListSerializer
        elif self.action == 'retrieve':
            return ClubsDetailSerializer
        return ClubsDetailSerializer

class PlayerModelViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    # serializer_class = PlayerDetailSerializer  # Set a default serializer
    lookup_field = 'playerid'

    def get_serializer_class(self):
        if self.action == 'list':
            return PlayerListSerializer
        elif self.action == 'retrieve':
            return PlayerDetailSerializer
        return PlayerDetailSerializer


class TeamModelViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    # serializer_class = TeamListSerializer  # Default serializer
    lookup_field = 'teamid'

    def get_serializer_class(self):
        if self.action == 'list':
            return TeamListSerializer
        elif self.action == 'retrieve':
            return TeamDetailSerializer
        return TeamDetailSerializer
    

class EventModelViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    # serializer_class = TeamDetailSerializer  # Default serializer
    lookup_field = 'eventid'

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        elif self.action == 'retrieve':
            return EventDetailSerializer
        return EventDetailSerializer
    

# class EventtournamentModelViewSet(viewsets.ModelViewSet):
#     queryset = Eventtournament.objects.all()
#     serializer_class = EventtournamentSerializer  # Default serializer
#     lookup_field = 'eventtournamentid'
    

class TournamenttypeModelViewSet(viewsets.ModelViewSet):
    queryset = Tournamenttype.objects.all()
    # serializer_class = TeamDetailSerializer  # Default serializer
    lookup_field = 'tournamenttypeid'

    def get_serializer_class(self):
        if self.action == 'list':
            return TournamenttypeListSerializer
        elif self.action == 'retrieve':
            return TournamenttypeDetailSerializer
        return TournamenttypeDetailSerializer
    

class TournamentModelViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    # serializer_class = TeamDetailSerializer  # Default serializer
    lookup_field = 'tournamentid'

    def get_serializer_class(self):
        if self.action == 'list':
            return TournamentListSerializer
        elif self.action == 'retrieve':
            return TournamentDetailSerializer
        return TournamentDetailSerializer
    

class TournamentdrawModelViewSet(viewsets.ModelViewSet):
    queryset = Tournamentdraw.objects.all()
    # serializer_class = TeamDetailSerializer  # Default serializer
    lookup_field = 'tournamentdrawid'

    def get_serializer_class(self):
        if self.action == 'list':
            return TournamentdrawListSerializer
        elif self.action == 'retrieve':
            return TournamentdrawDetailSerializer
        return TournamentdrawDetailSerializer