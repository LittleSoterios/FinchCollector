from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finch_index, name='finches'),
    path('finches/<int:finch_id>', views.finch_detail, name='detail'),
    path('finches/create/', views.FinchesCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update', views.FinchesUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete', views.FinchesDelete.as_view(), name='finches_delete'),

]