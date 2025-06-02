from django.contrib import admin

from .models import Project, TimeEntry
# Register your models here.


class TimeEntryInline(admin.TabularInline):
    model = TimeEntry
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [TimeEntryInline]


admin.site.register(Project, ProjectAdmin)
