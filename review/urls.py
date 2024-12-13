from django.urls import path,include
from .views import SignupView, LoginView, SessionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'sessions', SessionViewSet, basename='sessions')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', SignupView.as_view(), name='auth_signup'),
    path('auth/login/', LoginView.as_view(), name='auth_login'),
]
