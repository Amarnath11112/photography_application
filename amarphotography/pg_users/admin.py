from django.contrib import admin
from .models import PG_users, pg_login, pg_roles, pg_permission

# Register your models here.
admin.site.register(PG_users)
admin.site.register(pg_login)
admin.site.register(pg_roles)
admin.site.register(pg_permission)