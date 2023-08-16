from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views.users_views import ActiveUsersListView
from ..views.worked_hours_views import WorkedHoursView

class TestUrls(SimpleTestCase):

    def test_active_users_list_resolves(self):
        url = reverse('active-users-list')
        self.assertEquals(url, '/v1/users')
        self.assertEquals(resolve(url).func.view_class, ActiveUsersListView)

    def test_worked_hours_resolves(self):
        dummy_user_id = 1234
        url = reverse('worked-hours', args=[dummy_user_id])
        self.assertEquals(url, f'/v1/users/{dummy_user_id}/worked_hours')
        self.assertEquals(resolve(url).func.view_class, WorkedHoursView)
