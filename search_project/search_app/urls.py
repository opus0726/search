from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('', views.ListView.as_view(), name='list'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('<int:book_id>/review/', views.CreateReviewView.as_view(), name='review'),
    path('search/',views.SearchView.as_view(), name="search"),
]
