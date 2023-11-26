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

from .models import Player, Team, Event, Clubs, Tournamenttype, Tournament, Tournamentdraw
from .serializers import (
    PlayerListSerializer, PlayerDetailSerializer, TeamListSerializer, TeamDetailSerializer,
    EventListSerializer, EventDetailSerializer, 
    ClubsListSerializer, ClubsDetailSerializer, TournamenttypeListSerializer, TournamenttypeDetailSerializer,
    TournamentListSerializer, TournamentDetailSerializer, TournamentdrawListSerializer, TournamentdrawDetailSerializer

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
    

# viewsets for custom SQL queries
class EventQueryParamsSerializer(serializers.Serializer):
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)

class EventDataSerializer(serializers.Serializer):
    EventType = serializers.CharField(max_length=100)
    EventTypeID = serializers.IntegerField()
    Division = serializers.CharField(max_length=100)
    EventYear = serializers.IntegerField()
    EventWeek = serializers.IntegerField()
    EventID = serializers.IntegerField()
    EventName = serializers.CharField(max_length=200)
    ShortName = serializers.CharField(max_length=100)
    City = serializers.CharField(max_length=100)
    Region = serializers.CharField(max_length=100)
    RegionPrefix = serializers.CharField(max_length=50)
    CountryFlag = serializers.URLField()
    LocalStartDate = serializers.DateField()
    LocalEndDate = serializers.DateField()
    LocalUTC = serializers.IntegerField()



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

        start_date_begin = data.get('start_date_begin', (datetime.now() - timedelta(days=30)).date())
        start_date_end = data.get('start_date_end', (datetime.now() + timedelta(days=30)).date())

        sql = """
            SELECT t.eventtype AS EventType, t.eventtypeid AS EventTypeID, t.division AS Division, e.eventyear AS EventYear, w.tourweek AS EventWeek, e.eventid AS EventID, e.eventname AS EventName, e.shortname AS ShortName, e.city AS City, s.section AS Region, s.prefix AS RegionPrefix, CONCAT('https://www.curlingzone.com/forums/images/flag/', e.sectionid, '_flag.gif') AS CountryFlag, e.startdate AS LocalStartDate, e.enddate AS LocalEndDate, x.offset AS LocalUTC
            FROM event e
            INNER JOIN eventlink AS l ON l.eventid = e.eventid
            INNER JOIN eventtype AS t ON t.eventtypeid = l.eventtypeid
            INNER JOIN eventweek_event AS w ON w.eventid = e.eventid AND w.eventtypeid = l.eventtypeid
            INNER JOIN section AS s ON s.sectionid = e.sectionid
            INNER JOIN timezone AS x ON x.timezoneid = e.timezoneid
            WHERE (l.eventtypeid = 81 OR l.eventtypeid = 82 OR l.eventtypeid = 85) AND e.eventyear = 2024
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



        


        

