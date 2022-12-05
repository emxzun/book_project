
from django.urls import path

from books import views
from books.views import *

urlpatterns = [
    path('', ListCreateBookApiView.as_view()),
    path('<int:pk>/', RetUpdDelBookApiView.as_view()),
    path('del/<int:pk>/', views.book_del_api_view),
]