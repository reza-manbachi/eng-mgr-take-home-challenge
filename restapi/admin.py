from django.contrib import admin
from .models.users import User
from .models.worked_hours import WorkedHour

class WorkedHourInline(admin.TabularInline):
    model = WorkedHour
    extra = 0  # This controls the number of empty forms to display for adding related records

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [WorkedHourInline]
