from rest_framework import serializers
from .models import Player, Team, Event
from django.db import models
from django.urls import reverse, NoReverseMatch


class PlayerListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['playerid', 'firstname', 'lastname', 'url']
        
        extra_kwargs = {
            'url': {'view_name': 'api:player-detail', 'lookup_field': 'playerid'}
        }


class PlayerDetailSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Player
        fields = '__all__'  # Include all other player fields along with teams
        extra_kwargs = {
            'url': {'view_name': 'api:player-detail', 'lookup_field': 'playerid'}
        }

    def get_teams(self, obj):
        related_teams = Team.objects.filter(
            models.Q(skip=obj) |
            models.Q(fourth=obj) |
            models.Q(third=obj) |
            models.Q(second=obj) |
            models.Q(lead=obj) |
            models.Q(spare=obj)
        ).distinct()

        # Pass the context to the TeamListSerializer
        return TeamListSerializer(related_teams, many=True, context=self.context).data



        

class TeamListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['teamid', 'city', '__str__', 'url']
        extra_kwargs = {
            'url': {'view_name': 'api:team-detail', 'lookup_field': 'teamid'}
        }


class TeamDetailSerializer(serializers.HyperlinkedModelSerializer):
    eventid = serializers.HyperlinkedRelatedField(
        view_name='api:event-detail',
        lookup_field='eventid',
        queryset=Event.objects.all(),
        # source='eventid'
    )
    skip = serializers.HyperlinkedRelatedField(
        view_name='api:player-detail',
        lookup_field='playerid',
        queryset=Player.objects.all(),
        # source='skip'
    )
    fourth = serializers.HyperlinkedRelatedField(
        view_name='api:player-detail',
        lookup_field='playerid',
        queryset=Player.objects.all(),
        # source='fourth'
    )
    third = serializers.HyperlinkedRelatedField(
        view_name='api:player-detail',
        lookup_field='playerid',
        queryset=Player.objects.all(),
        # source='third'
    )
    second = serializers.HyperlinkedRelatedField(
        view_name='api:player-detail',
        lookup_field='playerid',
        queryset=Player.objects.all(),
        # source='second'
    )
    lead = serializers.HyperlinkedRelatedField(
        view_name='api:player-detail',
        lookup_field='playerid',
        queryset=Player.objects.all(),
        # source='lead'
    )
    spare = serializers.HyperlinkedRelatedField(
        view_name='api:player-detail',
        lookup_field='playerid',
        queryset=Player.objects.all(),
        # source='spare'
    )

        


    class Meta:
        model = Team
        fields = [
            'teamid', 'eventid', 'eventtypeid', 'drawid', 'status', 'fiveplayerteam', 'teamage', 'teamname_playerid', 
            'skip', 'fourth', 'third', 'second', 'lead', 'spare', 'coach', 'website', 'blogrss', 'twitter', 
            'twitter_rating', 'facebook', 'facebook_rating', 'facebookrss', 'youtube', 'city', 'sectionid', 
            'clubid', 'teamname', 'teamname_short', 'counter', 'dateline', 'submittedby', 'submittedemail', 
            'paid', 'paid_comments', 'sponsor', 'sponsorurl', 'photo', 'photodesc', 'tier', 'notes'
        ]
        extra_kwargs = {
            'url': {'view_name': 'api:team-detail', 'lookup_field': 'teamid'}
        }


    def get_player_field(self, obj, player_role):
        player = getattr(obj, player_role, None)
        if player:
            player_data = PlayerListSerializer(player, context=self.context).data
            player_data['position'] = player_role
            return player_data
        return None

    def get_skip(self, obj):
        return self.get_player_field(obj, 'skip')

    def get_fourth(self, obj):
        return self.get_player_field(obj, 'fourth')

    def get_third(self, obj):
        return self.get_player_field(obj, 'third')

    def get_second(self, obj):
        return self.get_player_field(obj, 'second')

    def get_lead(self, obj):
        return self.get_player_field(obj, 'lead')

    def get_spare(self, obj):
        return self.get_player_field(obj, 'spare')


class EventListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['eventname', 'startdate', 'enddate', 'url']
        extra_kwargs = {
            'url': {'view_name': 'api:event-detail', 'lookup_field': 'eventid'}
        }


class EventDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'  # Or customize the fields as needed
        extra_kwargs = {
            'url': {'view_name': 'api:event-detail', 'lookup_field': 'eventid'}
        }

        