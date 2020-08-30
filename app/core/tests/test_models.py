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
            email=email,
            password=password,
            name=name,
            height=height,
            weight=weight,
            age=age
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.name, name)
        self.assertEqual(user.age, age)
        self.assertEqual(user.height, height)
        self.assertEqual(user.weight, weight)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_invalid_email_raises_error(self):
        with self.assertRaises(ValueError):
            password = '123'
            get_user_model().objects.create_user(
                email=None,
                password=password
            )

    def test_create_super_user_sucessfully(self):
        email= "dummyEmail@gmail.com"
        password = "dummyPassword"
        super_user = get_user_model().objects.create_super_user(
            email=email,
            password=password
        )

        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
