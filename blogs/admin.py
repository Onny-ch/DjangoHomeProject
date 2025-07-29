from django.contrib import admin
from .models import Blogs


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "preview",
        "created_at",
        "publication_sign",
        "views_counter",
    )
    list_filter = (
        "publication_sign",
        "created_at",
    )
    search_fields = (
        "title",
        "created_at",
    )
