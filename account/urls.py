from django.urls import path

from account.views import RegisterApiView, LoginApiView, LogoutApiView, ChangePasswordApiView, ActivationApiView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('logout/', LogoutApiView.as_view()),
    path('change_password/', ChangePasswordApiView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationApiView.as_view())
]