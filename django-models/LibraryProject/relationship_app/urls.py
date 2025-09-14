# relationship_app/urls.py

from django.urls import path

from Introduction_to_Django.LibraryProject.bookshelf import views
from .views import LibraryDetailView

urlpatterns = [
    
    path('litBook/', views.book_list, name='listBook'),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
]
