import django_filters

from .models import Usage
from .models import UsageTypes


class UsageFilter(django_filters.FilterSet):
    amount = django_filters.CharFilter(field_name="amount")
    usage_at_to = django_filters.DateTimeFilter(
        field_name="usage_at",
        lookup_expr="lte",
    )
    usage_at_from = django_filters.DateTimeFilter(
        field_name="usage_at",
        lookup_expr="gt",
    )
    usage_at = django_filters.DateTimeFilter(field_name="usage_at")
    ordering = django_filters.OrderingFilter(
        fields=("amount", "usage_at"),
    )

    class Meta:
        model = Usage
        fields = []


class UsageTypesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name")
    unit = django_filters.CharFilter(field_name="unit")
    factor = django_filters.CharFilter(field_name="factor")
    ordering = django_filters.OrderingFilter(
        fields=("name", "unit", "factor"),
    )

    class Meta:
        model = UsageTypes
        fields = []
