"""
URL configuration for music_messenger_daw project.

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
# from django.contrib import admin
# music_messenger_daw/urls.py
from django.urls import path
from messaging.views import SendMessageView, GetMessagesView
from media.views import UploadMediaFileView, DownloadMediaFileView
from daw.views import CreateProjectView, GetProjectView, SaveProjectView
from accounts.views import UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    # path('admin/', admin.site.urls),
    #user
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/logout/', UserLogoutView.as_view(), name='logout'),
    # ********* need update profile *********
    #messages
    path('api/messages/send/', SendMessageView.as_view(), name="send_message"),
    path('api/messages/', GetMessagesView.as_view(), name="get_messages"),
    #media
    path('api/media/upload/', UploadMediaFileView.as_view(), name="upload_media"),
    path('api/media/<int:file_id>/', DownloadMediaFileView.as_view(), name="download_media"),
    #projects
    path('api/daw/project/create/', CreateProjectView.as_view(), name="create_project"),
    path('api/daw/project/<int:project_id>/', GetProjectView.as_view(), name="get_project"),
    path('api/daw/project/<int:project_id>/save/', SaveProjectView.as_view(), name="save_project"),
]
