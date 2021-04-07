import django_filters
from django_filters import rest_framework as filters
from api.models import Organization

class OrganizationFilter(filters.FilterSet):
    choices  = [
        ('Technology', 'Technology'),
        ('Education', 'Education'),
        ('Environment', 'Environment'),
        ('Humanities', 'Humanities'),
        ('Arts', 'Arts'),
        ('Business', 'Business'),
        ('Politics', 'Politics')
    ]
    name = django_filters.CharFilter(field_name = 'name', lookup_expr='istartswith', label='Name')
    dateEst = django_filters.NumberFilter(field_name='dateEstablished', lookup_expr='year', label='Date Est.')
    dateEst_gte = django_filters.NumberFilter(field_name='dateEstablished', lookup_expr='year__gte', label='Date Est Gtr Than' )
    dateEst_lte = django_filters.NumberFilter(field_name='dateEstablished', lookup_expr='year__lte', label='Date Est Lsr Than')
    
    city = django_filters.CharFilter(field_name='city', lookup_expr='istartswith', label='City')

    state = django_filters.CharFilter(field_name = 'state', lookup_expr = 'istartswith', label='State')
    country = django_filters.CharFilter(field_name = 'country', lookup_expr = 'istartswith', label='Country')
    domain = django_filters.ChoiceFilter(field_name='domain', label='Domain', choices=choices)
    orgHead = django_filters.CharFilter(field_name='orgHead', lookup_expr='istartswith', label='Org Head')
    numMembers = django_filters.NumberFilter(field_name='numMembers', label='Number Of Member')
    numMembers_lt = django_filters.NumberFilter(field_name='numMembers', lookup_expr='lt', label='No. Member Lsr Than')
    numMembers_gt = django_filters.NumberFilter(field_name='numMembers', lookup_expr='gt', label='No. Member Gtr Than')


    class Meta:
        model = Organization
        fields = '__all__'