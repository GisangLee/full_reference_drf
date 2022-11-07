from django.contrib import admin

from app.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
