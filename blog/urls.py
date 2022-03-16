from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('study_history/', views.study_history),
    # path('<int:pk>/', views.single_post_page),
]
