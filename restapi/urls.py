from django.contrib import admin
from django.urls import path
from .views.users_views import ActiveUsersListView
from .views.worked_hours_views import WorkedHoursView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/users', ActiveUsersListView.as_view(), name='active-users-list'),
    path('v1/users/<int:user_id>/worked_hours', WorkedHoursView.as_view(), name='worked-hours'),
]
