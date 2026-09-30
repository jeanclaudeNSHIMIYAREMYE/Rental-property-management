from django.test import TestCase

from apps.users.models import User


class UserModelTest(TestCase):

    def test_create_tenant(self):
        user = User.objects.create_user(
            username="tenant1",
            email="tenant@example.com",
            password="Password123!",
            role=User.Role.TENANT,
        )

        self.assertEqual(
            user.role,
            User.Role.TENANT
        )

        self.assertTrue(
            user.check_password("Password123!")
        )