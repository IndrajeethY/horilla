"""
kite_automations/filters.py
"""

from kite.filters import kitefilterset, django_filters
from kite_automations.models import MailAutomation


class AutomationFilter(kitefilterset):
    """
    AutomationFilter
    """

    search = django_filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = MailAutomation
        fields = "__all__"
