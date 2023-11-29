from rest_framework import serializers
from .models import Player, Team, Event, Eventlink, Tournamenttype, Tournament, Tournamentdraw, Clubs
from django.db import models
from django.urls import reverse, NoReverseMatch


class ClubsListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clubs
        fields = ['clubid', 'name', 'city', 'province', 'country', 'sheets', 'url']
        extra_kwargs = {
            'url': {'view_name': 'api:clubs-detail', 'lookup_field': 'clubid'}
        }


class ClubsDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clubs
        fields = '__all__'  # Or customize the fields as needed
        extra_kwargs = {
            'url': {'view_name': 'api:clubs-detail', 'lookup_field': 'clubid'}
        }



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
        fields = [field.name for field in Team._meta.fields] + ['skip', 'fourth', 'third', 'second', 'lead', 'spare']
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
    rr_tournamentid = serializers.SerializerMethodField(read_only=True)
    tb_tournamentid = serializers.SerializerMethodField(read_only=True)
    po_tournamentid = serializers.SerializerMethodField(read_only=True)
    rr_tournamentid_url = serializers.SerializerMethodField(read_only=True)
    tb_tournamentid_url = serializers.SerializerMethodField(read_only=True)
    po_tournamentid_url = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Event
        fields = '__all__'  # Or customize the fields as needed
        extra_kwargs = {
            'url': {'view_name': 'api:event-detail', 'lookup_field': 'eventid'}
        }

    # get the  rr_tournamentid, tb_tournamentid, and po_tournamentid fields from the Eventlink model
    # and return the tournamentid values for each
    def get_tournament_id(self, event_link, field_name):
        # print(f"get_tournament_id: {event_link} {field_name}")

        try: 
            tournament_link = getattr(event_link, field_name, None)
        except Exception as e:
            # print(f"Exception: {e}")
            return None

        # Check if tournament_link is None or 0 (indicating no valid foreign key)
        if tournament_link is None or tournament_link.pk == 0:
            return None

        try:
            # Fetch the tournament and return its ID if it exists
            return Tournament.objects.get(pk=tournament_link.pk).tournamentid
        except Tournament.DoesNotExist:
            return None

    def get_rr_tournamentid(self, obj):
        event_link = Eventlink.objects.filter(eventid=obj).first()
        return self.get_tournament_id(event_link, 'rr_tournamentid') if event_link else None

    def get_tb_tournamentid(self, obj):
        event_link = Eventlink.objects.filter(eventid=obj).first()
        return self.get_tournament_id(event_link, 'tb_tournamentid') if event_link else None

    def get_po_tournamentid(self, obj):
        event_link = Eventlink.objects.filter(eventid=obj).first()
        return self.get_tournament_id(event_link, 'po_tournamentid') if event_link else None
    
    def get_rr_tournamentid_url(self, obj):
        event_link = Eventlink.objects.filter(eventid=obj).first()
        tournament_id = self.get_tournament_id(event_link, 'rr_tournamentid')
        
        if tournament_id:
            url_path = reverse("api:tournament-detail", args=[tournament_id])
            base_url = self.context['request'].build_absolute_uri('/')[:-1]
            return base_url + url_path
        return None
    
    def get_tb_tournamentid_url(self, obj):
        event_link = Eventlink.objects.filter(eventid=obj).first()
        tournament_id = self.get_tournament_id(event_link, 'tb_tournamentid')
        if tournament_id:
            url_path = reverse("api:tournament-detail", args=[tournament_id])
            base_url = self.context['request'].build_absolute_uri('/')[:-1]
            return base_url + url_path
        return None
    
    def get_po_tournamentid_url(self, obj):
        event_link = Eventlink.objects.filter(eventid=obj).first()
        tournament_id = self.get_tournament_id(event_link, 'po_tournamentid')
        if tournament_id:
            url_path = reverse("api:tournament-detail", args=[tournament_id])
            base_url = self.context['request'].build_absolute_uri('/')[:-1]
            return base_url + url_path
        return None

class TournamenttypeListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournamenttype
        fields = ['tournamenttypeid', 'tournamenttype', 'url']
        extra_kwargs = {
            'url': {'view_name': 'api:tournamenttype-detail', 'lookup_field': 'tournamenttypeid'}
        }


class TournamenttypeDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournamenttype
        fields = '__all__'  # Or customize the fields as needed
        extra_kwargs = {
            'url': {'view_name': 'api:tournamenttype-detail', 'lookup_field': 'tournamenttypeid'}
        }


class TournamentListSerializer(serializers.HyperlinkedModelSerializer):
    tournamenttypeid = serializers.HyperlinkedRelatedField(
        view_name='api:tournamenttype-detail',
        lookup_field='tournamenttypeid',
        queryset=Tournamenttype.objects.all(),
        # source='tournamenttypeid'
    )
    class Meta:
        model = Tournament
        fields = ['tournamentid', 'tournamentname', 'tournamenttypeid', 'tournamentyear', 'url']
        extra_kwargs = {
            'url': {'view_name': 'api:tournament-detail', 'lookup_field': 'tournamentid'}
        }


class TournamentDetailSerializer(serializers.HyperlinkedModelSerializer):
    tournamenttypeid = serializers.HyperlinkedRelatedField(
        view_name='api:tournamenttype-detail',
        lookup_field='tournamenttypeid',
        queryset=Tournamenttype.objects.all(),
        # source='tournamenttypeid'
    )

    class Meta:
        model = Tournament
        fields = [field.name for field in Tournament._meta.fields] + ['tournamenttypeid']
        extra_kwargs = {
            'url': {'view_name': 'api:tournament-detail', 'lookup_field': 'tournamentid'}
        }


class TournamentdrawListSerializer(serializers.HyperlinkedModelSerializer):
    tournamentid = serializers.HyperlinkedRelatedField(
        view_name='api:tournament-detail',
        lookup_field='tournamentid',
        queryset=Tournament.objects.all(),
        # source='tournamentid'
    )
    class Meta:
        model = Tournamentdraw
        fields = ['tournamentid', 'drawid', 'drawname', 'drawdatetime', 'url']
        extra_kwargs = {
            'url': {'view_name': 'api:tournamentdraw-detail', 'lookup_field': 'tournamentid'}
        }


class TournamentdrawDetailSerializer(serializers.HyperlinkedModelSerializer):
    tournamentid = serializers.HyperlinkedRelatedField(
        view_name='api:tournament-detail',
        lookup_field='tournamentid',  # TODO: actually an eventid value
        queryset=Tournament.objects.all(),
        # source='tournamentid'
    )
    class Meta:
        model = Tournamentdraw
        fields = [field.name for field in Tournamentdraw._meta.fields] + ['tournamentid']
        extra_kwargs = {
            'url': {'view_name': 'api:tournamentdraw-detail', 'lookup_field': 'tournamentid'}
        }

        
# viewsets for custom SQL queries
class EventQueryParamsSerializer(serializers.Serializer):
    start_date_begin = serializers.DateField(required=False)
    start_date_end = serializers.DateField(required=False)

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