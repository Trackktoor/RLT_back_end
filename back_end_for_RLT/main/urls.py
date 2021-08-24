from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create_new_project', views.create_new_project.as_view(), name='create_new_project'),
    path('create_new_participant', views.create_new_participant.as_view(), name='create_new_participant'),
    path('pinning_participant', views.pinning_participant.as_view(), name='pinning_participant'),
    path('get_info_for_project', views.get_info_for_project.as_view(), name='get_info_for_project'),
    path('send_message_in_telegram_chat', views.send_message_in_telegram_chat.as_view(), name='send_message_in_telegram_chat'),
    path('get_messages_for_telegram_chat', views.get_messages_for_telegram_chat.as_view(), name='get_messages_for_telegram_chat'),
    path('create_new_client/<str:cache>', views.create_new_client.as_view(),name='create_new_client'),
    path('create_new_entry_for_chronicle', views.create_new_entry_for_chronicle.as_view(), name='create_new_entry_for_chronicle'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)