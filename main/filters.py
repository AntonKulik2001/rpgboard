from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from django.forms import DateTimeInput


from .models import *

class RespFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='date',
        lookup_expr='lt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type':'datetime-local'},
        ),
    )

    class Meta:
        model = UserResponse
        fields = {
            'text': ['icontains'],
        }
