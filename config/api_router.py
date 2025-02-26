from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path

from cz_api.users.api.views import UserViewSet
from cz.views import (
    PlayerModelViewSet,
    TeamModelViewSet,
    EventModelViewSet,
    ClubsModelViewSet,
    TournamenttypeModelViewSet,
    TournamentModelViewSet,
    TournamentdrawModelViewSet,
    ScoreGameModelViewSet,
    TournamentGameModelViewSet,
    CurrentEventsViewSet,
    UpcomingEventsViewSet,
    LiveGamesViewSet,
    RecentResultsViewSet,
    EventScheduleViewSet,
    PlayerStatsViewSet,
    TeamStatsViewSet,
    StandingsViewSet,
    # EventInfoViewSet,
    # EventTeamsViewSet,
    EventInfoViewset,
)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("clubs", ClubsModelViewSet, basename='clubs')
router.register("players", PlayerModelViewSet, basename='player')
router.register("teams", TeamModelViewSet, basename='team')
router.register("events", EventModelViewSet, basename='event')
# router.register("eventtournaments", EventtournamentModelViewSet, basename='eventtournament')
router.register("tournamenttypes", TournamenttypeModelViewSet, basename='tournamenttype')
router.register("tournaments", TournamentModelViewSet, basename='tournament')
router.register("tournamentdraws", TournamentdrawModelViewSet, basename='tournamentdraw')
router.register("scoregames", ScoreGameModelViewSet, basename='scoregame')
router.register("tournamentgames", TournamentGameModelViewSet, basename='tournamentgame')
router.register("current-events", CurrentEventsViewSet, basename='current-events')
router.register("upcoming-events", UpcomingEventsViewSet, basename='upcoming-events')
router.register("live-games", LiveGamesViewSet, basename='live-games')
router.register("recent-results", RecentResultsViewSet, basename='recent-results')
router.register("event-schedule", EventScheduleViewSet, basename='event-schedule')
router.register("player-stats", PlayerStatsViewSet, basename='player-stats')
router.register("team-stats", TeamStatsViewSet, basename='team-stats')
router.register("standings", StandingsViewSet, basename='standings')
router.register("eventinfo", EventInfoViewset, basename='eventinfo')
# router.register("eventteams", EventTeamsViewSet, basename='eventteams')



app_name = "api"
urlpatterns = router.urls

# urlpatterns += [
#     path('eventinfo/', EventInfoView.as_view(), name='eventinfo'),
# ]
