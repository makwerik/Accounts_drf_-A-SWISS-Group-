from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UsersSerializer
from .models import Users
from django.db.models import Q  # Q-объекты из Django, чтобы строить сложные запросы с использованием логических операторов (AND, OR)
from rest_framework import generics  # generics из Django REST Framework, которые предоставляют набор базовых классов представлений.




# Create your views here.

class UserCreateApiView(APIView):
    """Представление для создания юзеров"""

    def post(self, request):
        device = request.headers.get('x-Device')  # Определяем тип устройства
        serializer = UsersSerializer(data=request.data)
        print(device)

        # Валидация данных
        if device == 'mobile':
            required_fields = ['phone_number']
        elif device == 'web':
            required_fields = ['last_name', 'first_name', 'birth_date', 'passport_number', 'birth_place', 'phone_number', 'registration_address']
        elif device == 'mail':
            required_fields = ['first_name', 'mail']
        else:
            return Response({"Ошибка": "Неверный x-Device"}, status=status.HTTP_400_BAD_REQUEST)


        # Проверяем наличие обязательных полей
        for field in required_fields:
            # Если поля нет, уведомляем об этом
            if not request.data.get(field):
                return Response({f"Отсутсвует обязательное поле": {field}}, status=status.HTTP_400_BAD_REQUEST)

        # Если всё прошло успешно - сохраняем данные
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserIdApiView(APIView):
    """Представление для поиска юзера по id"""

    def get(self, request):
        userid = request.query_params.get('userid')
        try:
            user = Users.objects.get(id=userid)

            serializer = UsersSerializer(user)

            return Response({f"Пользователь": serializer.data})
        except:
            return Response({"Ошибка": "Пользователь не найден"}, status=status.HTTP_400_BAD_REQUEST)



class UserSearchApiView(generics.ListAPIView):
    """Представление для поиска юзера по одному или нескольким полям: фамилия, имя, отчество, телефон, email."""

    serializer_class = UsersSerializer  # Для этого представления используется сериализатор UserSerializer.

    def get_queryset(self):  # Переопределяю метод get_queryset, который отвечает за получение набора данных,
        # которые будут возвращены.

        queryset = Users.objects.all()
        query_params = self.request.GET # Получаем переданные данные в параметры запроса

        # Извлекаю значение параметров запроса, если они есть. Если нет - возвращается None
        last_name = query_params.get('last_name')
        first_name = query_params.get('first_name')
        middle_name = query_params.get('middle_name')
        phone_number = query_params.get('phone_number')
        mail = query_params.get('mail')

        filters = Q()  # Складируем фильтры полученные

        # Проверяю каждый из параметров и добавляю в фильтры, если параметры присутствуют ( тем самым получая список условий)
        if last_name:
            filters &= Q(last_name__icontains=last_name)
        if first_name:
            filters &= Q(first_name__icontains=first_name)
        if middle_name:
            filters &= Q(middle_name__icontains=middle_name)
        if phone_number:
            filters &= Q(phone_number__icontains=phone_number)
        if mail:
            filters &= Q(email__icontains=mail)

        return queryset.filter(filters)  # Применяю фильтры и возвращаю отфильтрованный набор данных
