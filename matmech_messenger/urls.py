from django.urls import path, re_path

from . import views

app_name = "matmech_messenger"
urlpatterns = [
    path('', views.main, name='main'),
    path('login', views.login),
    path('me/', views.my_account),
    path('chats/', views.my_chats),
    path('chats/private/', views.private_chats),
    path('guests/', views.all_guests),
    path('guest/<int:guest_id>/', views.account),
    path('guest/<int:guest_id>/chat/', views.private_chat),
    path('guest/<int:guest_id>/chat/<int:message_id>/', views.private_chat_message),
    path('guest/<int:guest_id>/chat/<int:message_id>/read/', views.private_chat_message_read),
    path('guest/<int:guest_id>/send_message', views.send_message),

]
