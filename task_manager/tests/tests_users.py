from django.test import TestCase
from task_manager.users.models import User
from django.urls import reverse


class CRUDTestsForUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            first_name='Andrey',
            last_name='Makarov',
            username='evisorexx',
            password='iseedeadpeople'
        )
        User.objects.create(
            first_name='Ruslan',
            last_name='Saffiulin',
            username='polyarnik',
            email='nastavnik@lol.ru',
            password='tineproidesh'
        )

    # For CREATION
    def test_SignUp(self):
        resp = self.client.get(reverse('users_create'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='users/create.html')

        resp = self.client.post(
            reverse('users_create'),
            {
                'first_name': 'Creation',
                'last_name': 'Test',
                'username': 'test_1',
                'password1': 'okigotadrip',
                'password2': 'okigotadrip',
            }
        )
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        user = User.objects.last()
        self.assertEqual(user.first_name, 'Creation')
        self.assertEqual(user.last_name, 'Test')
        self.assertEqual(user.username, 'test_1')

        resp = self.client.get(reverse('users_list'))
        self.assertTrue(len(resp.context['users']) == 3)

    # For READ
    def test_ListUsers(self):
        resp = self.client.get(reverse('users_list'))
        self.assertTrue(len(resp.context['users']) == 2)

    # For UPDATE
    def test_UpdateUser(self):
        user = User.objects.get(id=1)
        resp = self.client.get(
            reverse('users_update', kwargs={'pk': user.id})
        )
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))

        self.client.force_login(user)

        resp = self.client.get(
            reverse('users_update', kwargs={'pk': user.id})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='users/update.html')
        resp = self.client.post(
            reverse('users_update', kwargs={'pk': user.id}),
            {
                'first_name': 'Not',
                'last_name': 'Today',
                'username': 'Anonymous',
                'password1': 'asdzxc321!',
                'password2': 'asdzxc321!',
            }
        )
        self.assertEqual(resp.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.username, 'Anonymous')

    # For DELETE
    def test_DeleteUser(self):
        user = User.objects.get(username='evisorexx')
        resp = self.client.get(reverse('users_delete', kwargs={'pk': user.id}))
        
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, reverse('login'))
        
        self.client.force_login(user)

        resp = self.client.get(reverse('users_delete', kwargs={'pk': user.id}))
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post(
            reverse('users_delete', kwargs={'pk': user.id})
        )
        self.assertRedirects(resp, expected_url=reverse('users_list'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(User.objects.count(), 1)