from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import connection
from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional, List
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from django.db import connection
from drf_spectacular.utils import extend_schema
from datetime import datetime
from pydantic import BaseModel, ValidationError, validator
from pydantic.fields import Field
from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes



from datetime import datetime, timedelta
from typing import Optional, List

from .models import Player, Team, Event, Clubs, Tournamenttype, Tournament, Tournamentdraw, Scoregame, Tournamentgame
from .serializers import (
    PlayerListSerializer, PlayerDetailSerializer, TeamListSerializer, TeamDetailSerializer,
    EventListSerializer, EventDetailSerializer, 
    ClubsListSerializer, ClubsDetailSerializer, TournamenttypeListSerializer, TournamenttypeDetailSerializer,
    TournamentListSerializer, TournamentDetailSerializer, TournamentdrawListSerializer, TournamentdrawDetailSerializer,
    ScoreGameListSerializer, ScoreGameDetailSerializer, 
    TournamentGameListSerializer, TournamentGameDetailSerializer,
    EventQueryParamsSerializer, EventDataSerializer
)
from .filters import ClubsFilter

class ClubsModelViewSet(viewsets.ModelViewSet):
    queryset = Clubs.objects.all()
    lookup_field = 'clubid'
    filterset_class = ClubsFilter

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


class ScoreGameModelViewSet(viewsets.ModelViewSet):
    queryset = Scoregame.objects.all()
    lookup_field = 'gameid'

    def get_serializer_class(self):
        if self.action == 'list':
            return ScoreGameListSerializer
        elif self.action == 'retrieve':
            return ScoreGameDetailSerializer
        return ScoreGameDetailSerializer


class TournamentGameModelViewSet(viewsets.ModelViewSet):
    queryset = Tournamentgame.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return TournamentGameListSerializer
        elif self.action == 'retrieve':
            return TournamentGameDetailSerializer
        return TournamentGameDetailSerializer


class CurrentEventsViewSet(viewsets.ViewSet):
    """Retrieve events that are currently happening (today is between start and end date)"""
    
    @extend_schema(
        description="Get tournaments/events that are currently active",
        responses={200: EventListSerializer(many=True)}
    )
    def list(self, request):
        today = datetime.now().date()
        current_events = Event.objects.filter(
            startdate__lte=today,
            enddate__gte=today
        ).order_by('startdate')
        
        serializer = EventListSerializer(
            current_events, 
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class UpcomingEventsViewSet(viewsets.ViewSet):
    """Retrieve events that will start in the next 30 days"""
    
    @extend_schema(
        description="Get tournaments/events that will start in the next 30 days",
        responses={200: EventListSerializer(many=True)}
    )
    def list(self, request):
        today = datetime.now().date()
        thirty_days_ahead = today + timedelta(days=30)
        
        upcoming_events = Event.objects.filter(
            startdate__gt=today,
            startdate__lte=thirty_days_ahead
        ).order_by('startdate')
        
        serializer = EventListSerializer(
            upcoming_events, 
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class LiveGamesViewSet(viewsets.ViewSet):
    """Retrieve games that are currently in progress"""
    
    @extend_schema(
        description="Get games that are currently in progress",
        responses={200: ScoreGameListSerializer(many=True)}
    )
    def list(self, request):
        # This is a basic implementation. In a real system, you'd have a field 
        # indicating if a game is live/in-progress
        # For now, we'll simulate this by looking at games from tournaments happening today
        
        today = datetime.now().date()
        
        # Find events happening today
        current_events = Event.objects.filter(
            startdate__lte=today,
            enddate__gte=today
        )
        
        # Get IDs for tournament draws associated with these events
        tournament_ids = []
        for event in current_events:
            tournament_ids.extend(list(Tournament.objects.filter(eventid=event.eventid).values_list('tournamentid', flat=True)))
        
        # Get games associated with these tournaments
        tournament_games = Tournamentgame.objects.filter(tournamentid__in=tournament_ids)
        game_ids = tournament_games.values_list('gameid', flat=True)
        
        # Get the actual games
        live_games = Scoregame.objects.filter(gameid__in=game_ids)
        
        serializer = ScoreGameListSerializer(
            live_games, 
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class RecentResultsViewSet(viewsets.ViewSet):
    """Retrieve games that have recently completed"""
    
    @extend_schema(
        description="Get games that have recently completed",
        responses={200: ScoreGameListSerializer(many=True)}
    )
    def list(self, request):
        # Similar to live games, we need to simulate this
        # In a real system, you'd have a completion date/time field
        
        today = datetime.now().date()
        seven_days_ago = today - timedelta(days=7)
        
        # Find events that ended in the last 7 days
        recent_events = Event.objects.filter(
            enddate__gte=seven_days_ago,
            enddate__lt=today
        )
        
        # Get IDs for tournaments associated with these events
        tournament_ids = []
        for event in recent_events:
            tournament_ids.extend(list(Tournament.objects.filter(eventid=event.eventid).values_list('tournamentid', flat=True)))
        
        # Get games associated with these tournaments
        tournament_games = Tournamentgame.objects.filter(tournamentid__in=tournament_ids)
        game_ids = tournament_games.values_list('gameid', flat=True)
        
        # Get the actual games
        recent_games = Scoregame.objects.filter(gameid__in=game_ids)
        
        serializer = ScoreGameListSerializer(
            recent_games, 
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)


class EventScheduleViewSet(viewsets.ViewSet):
    """Retrieve the schedule of games for a specific event"""
    
    @extend_schema(
        description="Get the schedule of games for a specific event",
        parameters=[
            OpenApiParameter(name="event_id", description="ID of the event", required=True, type=int)
        ],
        responses={200: ScoreGameListSerializer(many=True)}
    )
    def list(self, request):
        event_id = request.query_params.get('event_id')
        if not event_id:
            return Response(
                {"error": "event_id parameter is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Find tournaments for this event
            tournaments = Tournament.objects.filter(eventid=event_id)
            tournament_ids = tournaments.values_list('tournamentid', flat=True)
            
            # Find games in these tournaments
            tournament_games = Tournamentgame.objects.filter(tournamentid__in=tournament_ids)
            game_ids = tournament_games.values_list('gameid', flat=True)
            
            # Get the actual games
            games = Scoregame.objects.filter(gameid__in=game_ids)
            
            serializer = ScoreGameListSerializer(
                games, 
                many=True,
                context={'request': request}
            )
            return Response(serializer.data)
            
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )


class PlayerStatsViewSet(viewsets.ViewSet):
    """Get statistics for a specific player"""
    
    @extend_schema(
        description="Get statistics for a specific player",
        parameters=[
            OpenApiParameter(name="player_id", description="ID of the player", required=True, type=int)
        ],
        responses={200: dict}
    )
    def list(self, request):
        player_id = request.query_params.get('player_id')
        if not player_id:
            return Response(
                {"error": "player_id parameter is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            player = Player.objects.get(pk=player_id)
            
            # Find teams where this player is a member
            teams = Team.objects.filter(
                models.Q(skip=player) |
                models.Q(fourth=player) |
                models.Q(third=player) |
                models.Q(second=player) |
                models.Q(lead=player) |
                models.Q(spare=player)
            ).distinct()
            
            team_ids = teams.values_list('teamid', flat=True)
            
            # Find games where these teams played
            games_as_team1 = Scoregame.objects.filter(teamid1__in=team_ids)
            games_as_team2 = Scoregame.objects.filter(teamid2__in=team_ids)
            
            total_games = games_as_team1.count() + games_as_team2.count()
            
            # In a real system, you'd calculate wins, losses, and other stats
            # For this demo, we'll return basic stats
            results = {
                "player": {
                    "playerid": player.playerid,
                    "name": f"{player.firstname} {player.lastname}",
                    "position": "Varies" # In reality, you'd determine their primary position
                },
                "stats": {
                    "total_games": total_games,
                    "teams": team_ids.count(),
                    # Additional stats would be calculated here in a real system
                }
            }
            
            return Response(results)
            
        except Player.DoesNotExist:
            return Response(
                {"error": f"Player with ID {player_id} not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )


class TeamStatsViewSet(viewsets.ViewSet):
    """Get statistics for a specific team"""
    
    @extend_schema(
        description="Get statistics for a specific team",
        parameters=[
            OpenApiParameter(name="team_id", description="ID of the team", required=True, type=int)
        ],
        responses={200: dict}
    )
    def list(self, request):
        team_id = request.query_params.get('team_id')
        if not team_id:
            return Response(
                {"error": "team_id parameter is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            team = Team.objects.get(pk=team_id)
            
            # Find games for this team
            games_as_team1 = Scoregame.objects.filter(teamid1=team_id)
            games_as_team2 = Scoregame.objects.filter(teamid2=team_id)
            
            total_games = games_as_team1.count() + games_as_team2.count()
            
            # Get player details
            players = {
                "skip": team.skip.firstname + " " + team.skip.lastname if team.skip else "Unknown",
                "fourth": team.fourth.firstname + " " + team.fourth.lastname if team.fourth else "Unknown",
                "third": team.third.firstname + " " + team.third.lastname if team.third else "Unknown",
                "second": team.second.firstname + " " + team.second.lastname if team.second else "Unknown",
                "lead": team.lead.firstname + " " + team.lead.lastname if team.lead else "Unknown"
            }
            
            if team.spare:
                players["spare"] = team.spare.firstname + " " + team.spare.lastname
            
            # In a real system, you'd calculate wins, losses, and other stats
            results = {
                "team": {
                    "teamid": team.teamid,
                    "name": str(team),
                    "city": team.city if team.city else "Unknown",
                    "players": players
                },
                "stats": {
                    "total_games": total_games,
                    # Additional stats would be calculated here in a real system
                }
            }
            
            return Response(results)
            
        except Team.DoesNotExist:
            return Response(
                {"error": f"Team with ID {team_id} not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )


class StandingsViewSet(viewsets.ViewSet):
    """Get standings for a specific event"""
    
    @extend_schema(
        description="Get standings for a specific event",
        parameters=[
            OpenApiParameter(name="event_id", description="ID of the event", required=True, type=int)
        ],
        responses={200: dict}
    )
    def list(self, request):
        event_id = request.query_params.get('event_id')
        if not event_id:
            return Response(
                {"error": "event_id parameter is required"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            event = Event.objects.get(pk=event_id)
            
            # Find tournaments for this event
            tournaments = Tournament.objects.filter(eventid=event_id)
            
            # For each tournament, collect team records
            standings = []
            
            for tournament in tournaments:
                # Get teams in this tournament
                tournament_games = Tournamentgame.objects.filter(tournamentid=tournament.tournamentid)
                game_ids = tournament_games.values_list('gameid', flat=True)
                
                # Get unique teams from these games
                team_ids = set()
                for game in Scoregame.objects.filter(gameid__in=game_ids):
                    team_ids.add(game.teamid1)
                    team_ids.add(game.teamid2)
                
                # For each team, calculate basic stats
                for team_id in team_ids:
                    if team_id == 0:  # Skip placeholder teams
                        continue
                        
                    team = Team.objects.get(pk=team_id)
                    
                    # Get games for this team in this tournament
                    team_games = Scoregame.objects.filter(
                        models.Q(teamid1=team_id) | models.Q(teamid2=team_id),
                        gameid__in=game_ids
                    )
                    
                    # In a real system, you'd calculate wins and losses
                    # For this demo, we'll just provide counts
                    standings.append({
                        "team": {
                            "teamid": team.teamid,
                            "name": str(team),
                            "city": team.city if team.city else "Unknown"
                        },
                        "tournament": tournament.tournamentname,
                        "games_played": team_games.count(),
                        # Wins, losses, and other stats would be calculated here
                    })
            
            return Response(standings)
            
        except Event.DoesNotExist:
            return Response(
                {"error": f"Event with ID {event_id} not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )




class EventInfoViewset(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving custom SQL query results.

    Retrieves a list of events with detailed information including event type, event ID, 
    division, event week, and more. This data is particularly tailored for curling events.

    Fields:
    - EventType (string): The type of the event, e.g., "World Team Ranking". Length: 0-50 characters.
    - EventTypeId (int): Unique identifier for the event type. Ranges from 81 to 90. 
        For example, 81 represents Men's, 82 represents Women's, 85 represents Mixed Doubles.
    - Division (string): Division of the event, e.g., "Men", "Women", "Mixed". Length: 0-10 characters.
    - EventWeek (int): The week number of the event within the year, ranging from 1 to 44.
    - EventName (string): The full name of the event, e.g., "AMJ Campbell Shorty Jenkins Classic". 
        Length: 0-100 characters.
    - ShortName (string): A shorter or abbreviated name of the event, e.g., "Shorty Jenkins". 
        Length: 0-50 characters.
    - EventId (int): Unique identifier for the event.
    - City (string): The city where the event is held, e.g., "Cornwall". Length: 0-50 characters.
    - Region (string): The region or country where the event is held, e.g., "Canada". 
        Length: 0-50 characters.
    - RegionPrefix (string): The abbreviated region or country prefix, e.g., "CAN". Length: 0-3 characters.
    - CountryFlag (string): URL to the country flag image, e.g., 
        "https://www.curlingzone.com/forums/images/flag/300_flag.gif". Length: 100 characters.
    - TeamsList (array of EventTeam objects): List of teams participating in the event.
    - TeamCountries (array of strings): List of countries from which the teams originate, 
        e.g., "Canada", "Japan", "United States".
    - LocalStartDate (date): The start date of the event in local time as a Unix timestamp.
    - LocalEndDate (date): The end date of the event in local time as a Unix timestamp.
    - LocalUTC (string): The local UTC offset for the event's time zone, based off GMT, 
        e.g., "-5.0". Length: 0-5 characters.

    Optional Query Parameters:
    - start_date_begin (date): The beginning date for filtering events. Format: YYYY-MM-DD.
    - start_date_end (date): The end date for filtering events. Format: YYYY-MM-DD.
    """

    @extend_schema(
        # description="Retrieves a list of events with detailed information including event type, event ID, division, event week, and more. This data is particularly tailored for curling events.",
        parameters=[
            OpenApiParameter(name="start_date_begin", description="The beginning date for filtering events. Format: YYYY-MM-DD.", required=False, type=str, location=OpenApiParameter.QUERY),
            OpenApiParameter(name="start_date_end", description="The end date for filtering events. Format: YYYY-MM-DD.", required=False, type=str, location=OpenApiParameter.QUERY),
        ],
        responses={200: EventDataSerializer(many=True)}
    )
    def list(self, request):
        serializer = EventQueryParamsSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        print(f"data: {data}")

        start_date_begin = data.get('start_date_begin', (datetime.now() - timedelta(days=30)).date())
        start_date_end = data.get('start_date_end', (datetime.now() + timedelta(days=30)).date())

        # print(f"start_date_begin: {start_date_begin}")
        # print(f"start_date_end: {start_date_end}")

        sql = """
            SELECT t.eventtype AS EventType, t.eventtypeid AS EventTypeID, t.division AS Division, e.eventyear AS EventYear, w.tourweek AS EventWeek, e.eventid AS EventID, e.eventname AS EventName, e.shortname AS ShortName, e.city AS City, s.section AS Region, s.prefix AS RegionPrefix, CONCAT('https://www.curlingzone.com/forums/images/flag/', e.sectionid, '_flag.gif') AS CountryFlag, e.startdate AS LocalStartDate, e.enddate AS LocalEndDate, x.offset AS LocalUTC
            FROM event e
            INNER JOIN eventlink AS l ON l.eventid = e.eventid
            INNER JOIN eventtype AS t ON t.eventtypeid = l.eventtypeid
            INNER JOIN eventweek_event AS w ON w.eventid = e.eventid AND w.eventtypeid = l.eventtypeid
            INNER JOIN section AS s ON s.sectionid = e.sectionid
            INNER JOIN timezone AS x ON x.timezoneid = e.timezoneid
            WHERE (l.eventtypeid = 81 OR l.eventtypeid = 82 OR l.eventtypeid = 85)
            AND e.startdate >= '%s' AND e.startdate <= '%s'
            ORDER BY EventTypeID ASC, EventWeek ASC
        """

        query = sql % (start_date_begin, start_date_end)

        # print(query)

        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            data = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        return Response(data)



        


        

