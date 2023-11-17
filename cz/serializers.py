from rest_framework import serializers
from .models import Player, Team


class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['playerid', 'firstname', 'lastname']
        extra_kwargs = {
            'url': {'view_name': 'player-detail', 'lookup_field': 'playerid'}
        }

class PlayerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

    def get_teams(self, obj):
        # Assuming you have a reverse relation set up from Team to Player
        teams = obj.teams_as_skip.all()  # Modify based on your related_name
        return TeamListSerializer(teams, many=True).data



        

class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['teamid', 'skip', 'city', 'name']
        extra_kwargs = {
            'url': {'view_name': 'team-detail', 'lookup_field': 'teamid'}
        }


class TeamDetailSerializer(serializers.ModelSerializer):
    players = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = '__all__'  # Or customize the fields as needed

    def get_players(self, obj):
        # Dictionary to hold player instances with their positions
        player_positions = {
            'skip': obj.skip,
            'fourth': obj.fourth,
            'third': obj.third,
            'second': obj.second,
            'lead': obj.lead,
            'spare': obj.spare
        }

        # Serialize the players with positions
        players_with_positions = []
        for position, player in player_positions.items():
            if player is not None:
                player_data = PlayerListSerializer(player).data
                player_data['position'] = position
                players_with_positions.append(player_data)

        return players_with_positions
