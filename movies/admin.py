from django.contrib import admin

from . import models


@admin.register(models.SearchTerm)
class SearchTermAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    pass