from django.urls import path
from .views import UserCreateApiView, UserIdApiView, UserSearchApiView

urlpatterns = [
    path('user_create/', UserCreateApiView.as_view(), name='user-create'),
    path('get_user_id/', UserIdApiView.as_view(), name='get-user-id'),
    path('search_user/', UserSearchApiView.as_view(), name='user-search'),

]