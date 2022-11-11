from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import DishType, Dish, Cook


class ModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="pizza")

        self.assertEqual(str(dish_type),
                         dish_type.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(username="Test",
                                                    first_name="Test name",
                                                    last_name="Test surname")

        self.assertEqual(str(cook),
                         f"{cook.username} "
                         f"({cook.first_name} "
                         f"{cook.last_name})")

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="TestName")

        dish = Dish.objects.create(name="Test",
                                   dish_type=dish_type,
                                   price=10)

        self.assertEqual(str(dish),
                         dish.name)

    def test_create_cook_with_years_of_experience(self):
        username = "Test"
        password = "test1234"
        years_of_experience = 14

        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience= years_of_experience)

        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)
