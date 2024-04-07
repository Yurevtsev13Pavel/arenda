from django.contrib import admin

from prof.models import Profile


# Register your models here.
@admin.register(Profile)
class Profile(admin.ModelAdmin):
    exclude = ['id']
