import django_filters

from stafflane.filters import StafflaneFilterSet
from whatsapp.models import WhatsappCredientials


class CredentialsViewFilter(StafflaneFilterSet):
    search = django_filters.CharFilter(
        field_name="meta_phone_number", lookup_expr="icontains"
    )

    class Meta:
        model = WhatsappCredientials
        fields = ["meta_phone_number", "search"]
