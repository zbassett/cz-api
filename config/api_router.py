from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from cz_api.users.api.views import UserViewSet
from cz.views import PlayerModelViewSet, TeamModelViewSet, EventModelViewSet, ClubsModelViewSet, TournamenttypeModelViewSet, TournamentModelViewSet, TournamentdrawModelViewSet

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


app_name = "api"
urlpatterns = router.urls
