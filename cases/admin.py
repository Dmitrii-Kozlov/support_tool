from django.contrib import admin
from .models import Case, Comment, AMOSModule


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'module', 'author', 'created', 'active', 'get_emails')
    list_editable = ('module', 'active')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'body', 'author')


@admin.register(AMOSModule)
class AMOSModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'apn', 'name')