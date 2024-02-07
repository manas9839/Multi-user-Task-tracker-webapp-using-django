from django.contrib import admin
from tasks.models import Tasks


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'creation_date', 'due_date','user')

# Register your models here.
admin.site.register(Tasks, TaskAdmin)