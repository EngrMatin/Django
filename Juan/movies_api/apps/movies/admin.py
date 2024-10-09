from django.contrib import admin
from .models import Movie

# admin.site.register(Movie)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "summary", "release_date", "directed_by", "running_time", "language", "is_private")
    list_filter = ("name",)
    search_fields = ("name",)
    list_per_page = 50
