from django.contrib import admin
from .models import Blog,Article

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("name","anonymos_bloger","bloger")
    list_editable = ("anonymos_bloger","bloger")
    list_filter = ("anonymos_bloger","bloger")
    search_fields = ("name","description")
    


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "blog",
        "is_active",
        "is_verify",
        "is_pin",
    )
    list_editable = (
        "is_active",
        "is_verify",
        "is_pin",
    )
    list_filter = (
        "is_active",
        "is_verify",
        "is_pin",
        "blog",
    )
    search_fields = (
        "title",
        "summary",
        "description",
        "author__username",
        "author__email",
    )
    prepopulated_fields = {
        "slug": ("title",),
    }
    autocomplete_fields = (
        "author",
        "blog",
    )

    ordering = (
        "-id",
    )
    fieldsets = (
        ("اطلاعات اصلی", {
            "fields": ("title", "slug", "summary", "description", "thumbnail"),
        }),
        ("ارتباطات", {
            "fields": ("author", "blog"),
        }),
        ("وضعیت مقاله", {
            "fields": ("is_active", "is_verify", "is_pin"),
        }),
    )