import django_filters
from .models import Clubs

class ClubsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    facility_type = django_filters.NumberFilter()
    sheets = django_filters.NumberFilter()
    min_sheets = django_filters.NumberFilter(field_name='sheets', lookup_expr='gte')
    max_sheets = django_filters.NumberFilter(field_name='sheets', lookup_expr='lte')
    weeks = django_filters.NumberFilter()
    rental_rate_per_day = django_filters.NumberFilter()
    leagues = django_filters.NumberFilter()

    address = django_filters.CharFilter(lookup_expr='icontains')
    mailaddress = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')
    province = django_filters.NumberFilter()
    country = django_filters.NumberFilter()
    postalcode = django_filters.CharFilter(lookup_expr='icontains')

    phone = django_filters.CharFilter(lookup_expr='icontains')
    fax = django_filters.CharFilter(lookup_expr='icontains')
    contact = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    website = django_filters.CharFilter(lookup_expr='icontains')
    blogrss = django_filters.CharFilter(lookup_expr='icontains')

    twitter = django_filters.CharFilter(lookup_expr='icontains')
    twitter_widget = django_filters.CharFilter(lookup_expr='icontains')
    twitter_rating = django_filters.NumberFilter()
    facebook = django_filters.CharFilter(lookup_expr='icontains')
    facebookrss = django_filters.CharFilter(lookup_expr='icontains')
    facebook_rating = django_filters.NumberFilter()

    googlemaps = django_filters.CharFilter(lookup_expr='icontains')
    logo = django_filters.NumberFilter()
    logosm = django_filters.NumberFilter()
    history = django_filters.CharFilter(lookup_expr='icontains')
    closed = django_filters.NumberFilter()
    origin = django_filters.NumberFilter()
    userid = django_filters.NumberFilter()

    class Meta:
        model = Clubs
        fields = '__all__'