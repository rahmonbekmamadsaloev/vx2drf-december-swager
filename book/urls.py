from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('books-viewset', BookViewSet)

urlpatterns = [
    path('api-view/', BookAPIView.as_view()),
    path('generic/', BookGenericAPIView.as_view()),
    path('list/', BookListAPIView.as_view()),
    path('create/', BookCreateAPIView.as_view()),
    path('list-create/', BookListCreateAPIView.as_view()),
    path('ret/<int:pk>/', BookRetrieveAPIView.as_view()),
    path('update/<int:pk>/', BookUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', BookDestroyAPIView.as_view()),
    path('ret-update/<int:pk>/', BookRetrieveUpdateAPIView.as_view()),
    path('ret-destroy/<int:pk>/', BookRetrieveDestroyAPIView.as_view()),
    path('rud/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),
    path('', include(router.urls)),
]
