from django.shortcuts import render
from rest_framework import viewsets

from .models import Player, Team
from .serializers import PlayerListSerializer, PlayerDetailSerializer, TeamListSerializer, TeamDetailSerializer


class PlayerModelViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PlayerListSerializer
        elif self.action == 'retrieve':
            return PlayerDetailSerializer
        return PlayerListSerializer


class TeamModelViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return TeamListSerializer
        elif self.action == 'retrieve':
            return TeamDetailSerializer
        return TeamListSerializer
    