from django.urls import path
from tutorial.quickstart import views

urlpatterns = [
    #path('', include('quickstart.urls')),
    path('api/books', views.books),
    path('api/books/', views.books),
    path('api/books/<int:pk>/', views.book),
    path('api/books/<int:pk>', views.book)
]