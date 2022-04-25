from django.urls import path

from . import views
from .views import MovieListView,MovieDetailView



urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetailView.as_view(), name='detail_list'),
]