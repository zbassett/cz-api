from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Player, Team, Event
from .serializers import (
    PlayerListSerializer, PlayerDetailSerializer, TeamListSerializer, TeamDetailSerializer,
    EventListSerializer, EventDetailSerializer
)


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