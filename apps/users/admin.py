from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Individual, Position, Company

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email']


admin.site.register(Individual)
admin.site.register(Position)
admin.site.register(Company)
