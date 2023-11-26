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
router.register("eventinfo", EventInfoViewset, basename='eventinfo')
# router.register("eventteams", EventTeamsViewSet, basename='eventteams')



app_name = "api"
urlpatterns = router.urls

# urlpatterns += [
#     path('eventinfo/', EventInfoView.as_view(), name='eventinfo'),
# ]
