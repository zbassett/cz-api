from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from cz_api.users.api.views import UserViewSet
from cz.views import PlayerModelViewSet, TeamModelViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("players", PlayerModelViewSet, basename='player')
router.register("teams", TeamModelViewSet)


app_name = "api"
urlpatterns = router.urls
