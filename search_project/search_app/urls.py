from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('', views.ListView.as_view(), name='list'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateItemView.as_view(), name='create'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:book_id>/review/', views.CreateReviewView.as_view(), name='review'),
    path('search/',views.SearchView.as_view(), name="search"),
    path('<int:book_id>/like/',views.LikeView.as_view(), name="like"),
    path('acp/',views.AcpView.as_view(), name="acp"),
]
