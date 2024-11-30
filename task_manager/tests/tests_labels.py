from django.test import TestCase
from task_manager.labels.models import Label
from task_manager.users.models import User
from django.urls import reverse


class CRUD_Label_Test(TestCase):
    def setUp(self):
        User.objects.create(
            first_name='Andrey',
            last_name='Makarov',
            username='evisorexx',
            password='iseedeadpeople'
        )

        self.user = User.objects.get(id=1)
        Label.objects.create(name='label1')
        Label.objects.create(name='label2')
        Label.objects.create(name='label3')

    def test_access(self):
        resp1 = self.client.get(reverse('label_create'))
        self.assertEqual(resp1.status_code, 302)
        resp2 = self.client.get(reverse('labels_list'))
        self.assertEqual(resp2.status_code, 302)
        resp3 = self.client.get(reverse('label_update', kwargs={'pk': 1}))
        self.assertEqual(resp3.status_code, 302)
        resp4 = self.client.get(reverse('label_delete', kwargs={'pk': 1}))
        self.assertEqual(resp4.status_code, 302)

        self.client.force_login(self.user)
        resp1 = self.client.get(reverse('label_create'))
        self.assertEqual(resp1.status_code, 200)
        resp2 = self.client.get(reverse('labels_list'))
        self.assertEqual(resp2.status_code, 200)
        resp3 = self.client.get(reverse('label_update', kwargs={'pk': 1}))
        self.assertEqual(resp3.status_code, 200)
        resp4 = self.client.get(reverse('label_delete', kwargs={'pk': 1}))
        self.assertEqual(resp4.status_code, 200)

    # For CREATE
    def test_CreateLabel(self):
        self.client.force_login(self.user)

        resp = self.client.post(reverse('label_create'), {'name': 'gavgav'})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('labels_list'))

        resp = self.client.get(reverse('labels_list'))
        self.assertTrue(len(resp.context['labels']) == 4)

    # For READ
    def test_Listlabel(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse('labels_list'))
        self.assertTrue(len(resp.context['labels']) == 3)

    # For UPDATE
    def test_UpdateLabel(self):
        self.client.force_login(self.user)
        s1 = Label.objects.get(pk=1)
        resp = self.client.post(reverse('label_update', kwargs={'pk': 1}),
                                {'name': 'Updated label'})
        self.assertEqual(resp.status_code, 302)
        s1.refresh_from_db()
        self.assertEqual(s1.name, 'Updated label')

    # For DELETE
    def test_DeleteStatus(self):
        self.client.force_login(self.user)
        self.assertEqual(Label.objects.count(), 3)
        resp = self.client.post(
            reverse('label_delete', kwargs={'pk': 3})
        )

        self.assertEqual(resp.status_code, 302)
        self.assertEqual(Label.objects.count(), 2)
        self.assertEqual(Label.objects.get(pk=1).name, 'label1')
        self.assertEqual(Label.objects.get(pk=2).name, 'label2')
