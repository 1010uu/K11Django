"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from boardApps import views

#URLConf파일을 2개로 사용하기 위해 board.urls를 인클루드 한다.
urlpatterns = [
    path('', views.main, name="main"),
    path('admin/', admin.site.urls),
    path('boardApps/', include('boardApps.urls')),
]

#첨부파일을 media폴더에 저장하기 위한 설정.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

