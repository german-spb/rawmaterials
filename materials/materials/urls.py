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
    path('total/filter_plastic/', views.filter_plastic),
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

    path('chipboard/', views.chipboard, name='chipboard'),
    path('chipboard/chipboard_edit/<int:id>/', views.chipboard_edit),
    path('chipboard_form/chipboard_edit/<int:id>/', views.chipboard_edit),
    path('chipboard_form/', views.chipboard_form),
    path('chipboard_form/chipboard_create/', views.chipboard_create),
    path('chipboard_delete_form/', views.chipboard_delete_form),
    path('chipboard_delete_form/chipboard_delete/', views.chipboard_delete),

    path('glue/', views.glue, name='glue'),
    path('glue_form/', views.glue_form),
    path('glue_form/glue_create/', views.glue_create),
    path('glue_form/glue_edit/<int:id>/', views.glue_edit),
    path('glue/glue_edit/<int:id>/', views.glue_edit),
    path('glue/search_glue/glue_edit/<int:id>/', views.glue_edit),
    path('glue/glue_documents/<int:id>/', views.glue_documents),
    path('glue/glue_notes/<int:id>/', views.glue_notes),
    path('glue/glue_notes/<int:id>/glue_notes_create/', views.glue_notes_create),
    path('glue/glue_documents/<int:id>/glue_notes/', views.glue_notes),

    path('glue_form/glue_documents/<int:id>/', views.glue_documents, name='glue_documents'),
    path('documents/<str:filename>/', views.glue_document_show, name='show_document'),
    path('glue/glue_documents/delete_document/<int:id>/', views.glue_delete_document, name='delete_document'),
    path('glue/glue_delete/', views.glue_delete, name='glue_delete'),
    path('glue_form/glue_delete/<int:id>/', views.glue_delete, name='glue_delete'),
    path('glue/search_glue/', views.search_glue),
    path('glue_form/search_glue/', views.search_glue),

    path('pack/', views.pack, name='pack'),
    path('pack/pack_search/', views.pack_search),
    path('pack_form/pack_search/', views.pack_search),
    path('pack_form/', views.pack_form),
    path('pack_form/pack_create/', views.pack_create),
    path('pack/pack_edit/<int:id>/', views.pack_edit),
    path('pack_form/pack_search/pack_edit/<int:id>/', views.pack_edit),
    path('pack/pack_search/pack_edit/<int:id>/', views.pack_edit),
    path('pack_form/pack_edit/<int:id>/', views.pack_edit),

    path('phone/', views.phone, name='phone'),
    path('phone_form/', views.phone_form),
    path('phone_form/phone_edit/<int:id>/', views.phone_edit),
    path('phone_form/phone_create/', views.phone_create),
    path('phone_form/phone_search/phone_edit/<int:id>/',views.phone_edit),
    path('phone/phone_edit/<int:id>/', views.phone_edit),
    path('phone/phone_form/phone_edit/<int:id>/', views.phone_edit),
    path('phone/phone_search/phone_edit/<int:id>/', views.phone_edit),
    path('phone/phone_search/', views.phone_search),
    path('phone_form/phone_search/', views.phone_search),
]
