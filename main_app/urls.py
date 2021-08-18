from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('clips/', views.clips_index, name='index'),
  path('clips/<int:clip_id>/', views.clips_detail, name='detail'),
  path('clips/create/', views.ClipCreate.as_view(), name='clips_create'),
  path('clips/<int:pk>/update/', views.ClipUpdate.as_view(), name='clips_update'),
  path('clips/<int:pk>/delete/', views.ClipDelete.as_view(), name='clips_delete'),
  path('clips/<int:clip_id>/add_comment/', views.add_comment, name='add_comment'),
  # path('toys/', views.ToyList.as_view(), name='toys_index'),
  # path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  # path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  # path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  # path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  # path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
]