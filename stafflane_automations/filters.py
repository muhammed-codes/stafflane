"""
stafflane_automations/filters.py
"""

from stafflane.filters import StafflaneFilterSet, django_filters
from stafflane_automations.models import MailAutomation


class AutomationFilter(StafflaneFilterSet):
    """
    AutomationFilter
    """

    search = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = MailAutomation
        fields = "__all__"
