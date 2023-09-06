from django.urls import path 
from . import views
urlpatterns = [
    path ('',views.home, name='home'), 
    path ('project_1/',views.project_1, name='project_1'), 
    path ('project_2/',views.project_2, name='project_2'), 
    path ('project_3/',views.project_3, name='project_3'), 
    path('contract', views.contract, name='Contract'),
    path('view_info/', views.view_info, name='view_info'),
]
