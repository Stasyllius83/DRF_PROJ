
from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentsListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name


urlpatterns = [
    path('payments/', PaymentsListAPIView.as_view(), name='payments_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_pair'),
]
