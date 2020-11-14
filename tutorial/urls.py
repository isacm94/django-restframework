from django.urls import path
from tutorial.quickstart import views

urlpatterns = [
    #path('', include('quickstart.urls')),
    path('books', views.books),
    path('books/', views.books),
    path('books/<int:pk>/', views.book),
    path('books/<int:pk>', views.book)
]