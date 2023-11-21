from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.db import models

from .models import Player, Team, Event, Eventtournament, Clubs, Tournamenttype, Tournament, Eventtournament, Tournamentdraw


class PlayerAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('__str__', 'firstname', 'lastname', 'homecity', 'homeprovince')
    # list_filter = ('firstname', 'lastname', 'homecity', 'homeprovince')
    search_fields = ('firstname', 'lastname', 'homecity', 'homeprovince')
    ordering = ('lastname', 'firstname', 'homecity', 'homeprovince')

    readonly_fields = ('related_teams',)

    def related_teams(self, obj):
        # Fetch teams related to this player
        related_teams = Team.objects.filter(
            models.Q(skip=obj) |
            models.Q(fourth=obj) |
            models.Q(third=obj) |
            models.Q(second=obj) |
            models.Q(lead=obj) |
            models.Q(spare=obj)
        ).distinct()

        # Build HTML for displaying links to related teams
        links = []
        for team in related_teams:
            url = reverse("admin:cz_team_change", args=[team.pk])  # Adjust 'app_team_change' according to your app's name and model
            links.append(format_html('<a href="{}">{}</a>', url, str(team)))

        return format_html('<br>'.join(links))

    related_teams.short_description = 'Related Teams'


class TeamAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('__str__', 'skip', 'third', 'second', 'lead', 'spare')
    # list_filter = ('country', 'created_at', 'updated_at')
    search_fields = ('skip__lastname', 'third__lastname', 'second__lastname', 'lead__lastname', 'spare__lastname')
    ordering = ('skip__lastname', 'third__lastname', 'second__lastname', 'lead__lastname', 'spare__lastname')


class EventAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('__str__', 'eventname', 'eventyear', 'startdate', 'enddate', 'city')
    # list_filter = ('country', 'created_at', 'updated_at')
    search_fields = ('eventname', 'eventyear', 'startdate', 'enddate', 'city')
    ordering = ('startdate', 'eventname', 'city')


class ClubsAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('name', 'city', 'province', 'country', 'sheets')
    # list_filter = ('country', 'created_at', 'updated_at')
    search_fields = ('name', 'city', 'province', 'country')
    ordering = ('name', 'city', 'province', 'country', 'sheets')


class EventtournamentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('__str__', 'eventid', 'tournamentid')
    # list_filter = ('country', 'created_at', 'updated_at')
    search_fields = ('eventid', 'tournamentid')
    ordering = ('eventid', 'tournamentid')


class TournamenttypeAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('tournamenttype', 'events')
    # list_filter = ('country', 'created_at', 'updated_at')
    search_fields = ('tournamenttype', 'events')
    ordering = ('tournamenttype', 'events')


class TournamentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('tournamentname', 'tournamentyear', 'tournamentdescription')
    # list_filter = ('country', 'created_at', 'updated_at')
    search_fields = ('tournamentname', 'tournamentyear', 'tournamentdescription')
    ordering = ('tournamentname', 'tournamentyear', 'tournamentdescription')


class TournamentdrawAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('tournamentid', 'drawname', 'drawdatetime')
    # list_filter = ('country', 'created_at', 'updated_at')
    search_fields = ('tournamentid', 'drawname', 'drawdatetime')
    ordering = ('tournamentid', 'drawname', 'drawdatetime')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Clubs, ClubsAdmin)
admin.site.register(Eventtournament, EventtournamentAdmin)
admin.site.register(Tournamenttype, TournamenttypeAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Tournamentdraw, TournamentdrawAdmin)