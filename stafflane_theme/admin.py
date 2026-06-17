"""
Admin registration for the stafflane_theme app
"""

from django.contrib import admin

from stafflane_theme.models import CompanyTheme, StafflaneColorTheme

# Register your stafflane_theme models here.
admin.site.register(StafflaneColorTheme)
admin.site.register(CompanyTheme)
