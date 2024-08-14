from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Users


# Create your tests here.


class UserCreateTests(APITestCase):

    def test_create_user_email(self):
        url = reverse('user-create')  # создание пользователя зарегистрировано под именем 'user-create' (Генерируем URL)
        data = {
            "first_name": "John",
            "mail": "johndoe@example.com"
        }
        response = self.client.post(url, data, format='json', HTTP_X_DEVICE='mail')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users.objects.count(), 1)  # Убеждаемся что пользователь создан в кол-во 1 юзера
        self.assertEqual(Users.objects.get().first_name,
                         'John')  # Проверяем, что имя пользователя совпадает с ожидаемым

    def test_create_user_mobile(self):
        url = reverse('user-create')
        data = {
            "phone_number": "79991234567"
        }
        response = self.client.post(url, data, format='json', HTTP_X_DEVICE='mobile')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users.objects.count(), 1)
        self.assertEqual(Users.objects.get().phone_number, '79991234567')

    def test_create_user_web(self):
        url = reverse('user-create')
        data = {
            "last_name": "Doe",
            "first_name": "John",
            "birth_date": "1990-01-01",
            "passport_number": "1234 567890",
            "birth_place": "City",
            "phone_number": "79991234567",
            "registration_address": "Address"
        }
        response = self.client.post(url, data, format='json', HTTP_X_DEVICE='web')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users.objects.count(), 1)
        self.assertEqual(Users.objects.get().last_name, 'Doe')

    def test_create_user_invalid_device(self):
        url = reverse('user-create')
        data = {
            "first_name": "John"
        }
        response = self.client.post(url, data, format='json', HTTP_X_DEVICE='invalid')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserIdApiViewTests(APITestCase):
    def setUp(self):
        # Создаем тестового пользователя с id=1
        self.user = Users.objects.create(
            first_name="John",
            last_name="Doe",
            phone_number="79991234567"
        )
        self.url = reverse('get-user-id')

    def test_get_user_by_id(self):
        data = {'userid': self.user.id}  # данные с ID пользователя
        response = self.client.get(self.url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверяем, что статус ответа 200 (OK)
        self.assertEqual(response.data['Пользователь']['first_name'],
                         self.user.first_name)  # Проверяем, что имя пользователя совпадает

    def test_get_user_by_invalid_id(self):
        data = {'userid': 999}
        response = self.client.get(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['Ошибка'],
                         "Пользователь не найден")  # Проверяем, что сообщение об ошибке корректное


class UserSearchTests(APITestCase):

    def setUp(self):  # создаем несколько пользователей для тестов.
        Users.objects.create(first_name="John", last_name="Doe", phone_number="79991234567")
        Users.objects.create(first_name="Jane", last_name="Doe", phone_number="79991234568")
        Users.objects.create(first_name="Jim", last_name="Beam", phone_number="79991234569")

    def test_search_user_by_first_name(self):
        url = reverse('user-search')
        response = self.client.get(url, {'first_name': 'John'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['first_name'], 'John')

    def test_search_user_by_last_name(self):
        url = reverse('user-search')
        response = self.client.get(url, {'last_name': 'Doe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_user_by_phone_number(self):
        url = reverse('user-search')
        response = self.client.get(url, {'phone_number': '79991234567'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['phone_number'], '79991234567')
