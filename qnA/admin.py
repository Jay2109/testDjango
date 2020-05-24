from django.contrib import admin
from . import models


@admin.register(models.Question)
class CustomQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "is_anonymous",
        "created_date",
        "updated_date",
    )


@admin.register(models.Answer)
class CustomQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "user",
        "is_anonymous",
        "created_date",
        "updated_date",
    )


@admin.register(models.Topic)
class CustomQuestionAdmin(admin.ModelAdmin):
    pass