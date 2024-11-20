from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.users.models import User


# Create your tests here.
class CRUDTestsForStatuses(TestCase):
    def setUp(self):
        User.objects.create(
            first_name='Andrey',
            last_name='Makarov',
            username='evisorexx',
            password='iseedeadpeople'
        )
        self.user = User.objects.get(id=1)
        Status.objects.create(name='status1')
        Status.objects.create(name='status2')
        Status.objects.create(name='status3')

    def test_access(self):
        resp1 = self.client.get(reverse('status_create'))
        self.assertEqual(resp1.status_code, 302)
        resp2 = self.client.get(reverse('statuses_list'))
        self.assertEqual(resp2.status_code, 302)
        resp3 = self.client.get(reverse('status_update', kwargs={'pk': 1}))
        self.assertEqual(resp3.status_code, 302)
        resp4 = self.client.get(reverse('status_delete', kwargs={'pk': 1}))
        self.assertEqual(resp4.status_code, 302)

        self.client.force_login(self.user)

        resp1 = self.client.get(reverse('status_create'))
        self.assertEqual(resp1.status_code, 200)
        resp2 = self.client.get(reverse('statuses_list'))
        self.assertEqual(resp2.status_code, 200)
        resp3 = self.client.get(reverse('status_update', kwargs={'pk': 1}))
        self.assertEqual(resp3.status_code, 200)
        resp4 = self.client.get(reverse('status_delete', kwargs={'pk': 1}))
        self.assertEqual(resp4.status_code, 200)

    # CREATE - Создание нового статуса
    def test_CreateStatus(self):
        self.client.force_login(self.user)

        resp = self.client.post(reverse('status_create'), {'name': 'status4'})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('statuses_list'))

        resp = self.client.get(reverse('statuses_list'))
        self.assertTrue(len(resp.context['statuses']) == 4)

    # READ - список всех статусов
    def test_ListStatus(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('statuses_list'))
        self.assertTrue(len(resp.context['statuses']) == 3)

    # UPDATE - обновление статуса
    def test_UpdateStatus(self):
        self.client.force_login(self.user)
        s1 = Status.objects.get(pk=1)
        resp = self.client.post(reverse('status_update', kwargs={'pk': 1}),
                                {'name': 'Updated Status'})
        self.assertEqual(resp.status_code, 302)
        s1.refresh_from_db()
        self.assertEqual(s1.name, 'Updated Status')

    # DELETE - удаление статуса
    def test_DeleteStatus(self):
        self.client.force_login(self.user)
        self.assertEqual(Status.objects.count(), 3)
        resp = self.client.post(
            reverse('status_delete', kwargs={'pk': 3})
        )
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Status.objects.count(), 2)
        self.assertEqual(Status.objects.get(pk=1).name, 'status1')
        self.assertEqual(Status.objects.get(pk=2).name, 'status2')