from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_successful(self):
        """Test creating a new user is successful"""
        email = 'david@gmail.com'
        password = 'testPassword'
        name = 'testName'
        age = 4
        height = 1.50
        weight = 40.25

        user = get_user_model().objects.create_user(
            email = email,
            password = password,
            name = name,
            height = height,
            weight= weight,
            age = age
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.name, name)
        self.assertEqual(user.age, age)
        self.assertEqual(user.height, height)
        self.assertEqual(user.weight, weight)
        self.assertTrue(user.check_password(password))
