from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.tasks.models import Task


class CRUDTestsForTasks(TestCase):

    def setUp(self):
        User.objects.create(
            first_name='Andrey',
            last_name='Makarov',
            username='evisorexx',
            password='iseedeadpeople'
        )

        self.user = User.objects.get(id=1)

        Status.objects.create(name='status1')
        self.status = Status.objects.get(id=1)

        print(f'Current user: {self.user}')

        Task.objects.create(
            id=1,
            name='Task',
            description='Do homework',
            author=self.user,
            executor=self.user,
            status=self.status,
        )

        self.task = Task.objects.get(id=1)
        print(f'Task info: {self.task}')

    url_tasks = [
        reverse('tasks_list'),
        reverse('task_create'),
        reverse('task_details', kwargs={'pk': 1}),
        reverse('task_update', kwargs={'pk': 1}),
        reverse('task_delete', kwargs={'pk': 1}),
    ]

    def test_access(self, urls=url_tasks):

        for url in urls:
            print(f"\nTesting URL without authentication: {url}")
            resp = self.client.get(url)
            print(f"Response status code: {resp.status_code}")
            self.assertRedirects(resp, f'/login/?next={url}')

        self.client.login(username='evisorexx', password='iseedeadpeople')

        for url in urls:
            print(f"\nTesting URL with authentication: {url}")
            resp = self.client.get(url)
            print(f"Response status code: {resp.status_code}")
            self.assertEqual(resp.status_code, 302)
