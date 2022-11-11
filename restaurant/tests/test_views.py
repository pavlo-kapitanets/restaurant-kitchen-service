from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from restaurant.models import DishType

DISH_TYPE_URL = reverse("restaurant:dish-type-list")


class PublicDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateManufacturerTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="Test",
            password="test1234")

        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="pizza")
        DishType.objects.create(name="pasta")

        dish_types = DishType.objects.all()

        response = self.client.get(DISH_TYPE_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["Dish_type_list"]),
                         list(dish_types))
        self.assertTemplateUsed(response, "restaurant/dish_type_list.html")
