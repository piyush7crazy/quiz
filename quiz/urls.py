from django.urls import path 
from . import views

urlpatterns=[
    path('api/create_quiz/',views.create_quiz_api,name="create_quiz_api"),
    path('api/list_quiz/',views.list_quiz_api,name="list_quiz_api"),
    path('api/detail_quiz/<int:id>/',views.detail_quiz_api,name="detail_quiz_api"),
    path('api/update_quiz/<int:id>/',views.update_quiz_api,name="update_quiz_api"),
    path('api/delete_quiz/<int:id>/',views.delete_quiz_api,name="delete_quiz_api"),
]