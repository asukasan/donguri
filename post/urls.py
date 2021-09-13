from django.urls import path, include
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_home, name='post_home'),
    path('detail/<int:id>/', views.post_detail, name='detail'),
    path('post_category/<int:id>', views.post_category, name='post_category'),
]
