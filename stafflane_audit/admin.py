"""
admin.py
"""

from django.contrib import admin

from stafflane_audit.models import AuditTag, StafflaneAuditInfo, StafflaneAuditLog

# Register your models here.

admin.site.register(AuditTag)
