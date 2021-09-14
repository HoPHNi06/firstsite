from django.urls import path
from . import views

urlpatterns = [
    path('search', views.SearchResultsView.as_view(), name='search'),
    path('', views.news_home, name='news_home'),
    path('add', views.news_add, name='news_add'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_view'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
    path('article/<int:pk>', views.ArticlesView.as_view(), name='article'),

]
