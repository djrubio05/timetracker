
from decimal import Decimal
import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Project, TimeEntry


class UserProjectDetailViewTest(TestCase):
    def setUp(self):
        # Create users
        self.user = User.objects.create_user(
            username="user1", password="pass123")
        self.other_user = User.objects.create_user(
            username="user2", password="pass456")
        # Create a project
        self.project = Project.objects.create(name="Test Project")
        # Create other project
        self.other_project = Project.objects.create(name="Other Test Project")
        # Create time entries
        self.entry1 = TimeEntry.objects.create(
            project=self.project,
            user=self.user,
            description="Task 1",
            worked_hours=Decimal("2.5"),
        )
        self.entry2 = TimeEntry.objects.create(
            project=self.project,
            user=self.user,
            description="Task 2",
            worked_hours=Decimal("1.0"),
        )
        self.entry3 = TimeEntry.objects.create(
            project=self.project,
            user=self.other_user,
            description="Task 3",
            worked_hours=Decimal("1.0"),
        )
        self.entry4 = TimeEntry.objects.create(
            project=self.other_project,
            user=self.other_user,
            description="Task 4",
            worked_hours=Decimal("3.0"),
        )

    def test_user_project_shows_only_target_user_entries(self):
        self.client.login(username="user1", password="pass123")
        url = reverse("timetracker:user_project",
                      args=[self.user.id, self.project.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Only target_user's entries for the project should be present
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")
        self.assertNotContains(response, "Task 3")
        self.assertNotContains(response, "Task 4")
        # Total hours should be correct
        self.assertEqual(
            response.context["total_hours_worked_by_user"], Decimal("3.50"))


class UserWeekDetailViewTest(TestCase):
    def setUp(self):
        # Create users
        self.user = User.objects.create_user(
            username="user1", password="pass123")
        self.other_user = User.objects.create_user(
            username="user2", password="pass456")
        # Create a project
        self.project = Project.objects.create(name="Test Project")
        # Create time entries
        self.entry1 = TimeEntry.objects.create(
            project=self.project,
            user=self.user,
            description="Task 1",
            worked_hours=Decimal("2.5"),
        )
        self.entry2 = TimeEntry.objects.create(
            project=self.project,
            user=self.user,
            description="Task 2",
            worked_hours=Decimal("1.0"),
        )
        self.entry3 = TimeEntry.objects.create(
            project=self.project,
            user=self.other_user,
            description="Task 3",
            worked_hours=Decimal("1.0"),
        )
        # Change Entry2 create_at time to minus 1 week
        past_week_time = timezone.now()-datetime.timedelta(weeks=1)
        self.entry2.created_at = past_week_time
        self.entry2.save()

    def test_user_shows_only_past_week_entries(self):
        self.client.login(username="user1", password="pass123")
        url = reverse("timetracker:user",
                      args=[self.user.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Only target_user's past week entries should be present
        self.assertContains(response, "Task 1")
        self.assertNotContains(response, "Task 2")
        self.assertNotContains(response, "Task 3")
        # Total hours for the week should be correct
        self.assertEqual(
            response.context["total_hours_worked_by_user"], Decimal("2.50"))
