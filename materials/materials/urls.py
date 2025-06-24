"""
URL configuration for materials project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from plastic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('plastic/', views.plastic),
    path('code_entry', views.code_entry),
    path('create/', views.create_plastic),
    path('list_code/', views.list_plastic ),
    path('list_result/', views.list_result ),
    path('total/', views.list_quantity ),
    path('input/', views.stock),
    path('input/stock/', views.input_stock),
    path('search/', views.search, name='search'),
    path('search/plastic/', views.search_plastic),
    path('form_delete/', views.form_delete),
    path('form_delete/delete/', views.delete),
    path('delete_result/', views.delete_result),
    path('delete_stock/', views.delete_stock),
    path('upload/', views.upload_file, name='upload_file'),
    path('upload_code/', views.upload_code, name='upload_code'),
    path('upload_result/', views.upload_result, name='upload_file'),
    path('excel/', views.to_excel),
    path('update/', views.input_update_code),
    path('update/update_fields/', views.input_update_code_fields),
    path('search/plastic/update_fields/', views.input_update_code_fields),
    path('download/<str:filename>/', views.download_file, name='download_file'),

    path('chipboard/', views.chipboard)

]
