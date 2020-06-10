from django.contrib import admin
from .models import Project, Tag


class ProjectAdmin(admin.ModelAdmin):
  filter_horizontal =('tag',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
