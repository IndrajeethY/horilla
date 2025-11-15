"""
admin.py
"""

from django.contrib import admin

from kite_audit.models import AuditTag, KiteAuditInfo, KiteAuditLog

# Register your models here.

admin.site.register(AuditTag)
