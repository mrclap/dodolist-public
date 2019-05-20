"""dodolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers

from app.views import apis, todo

router = routers.DefaultRouter()

router.register(r'categories', apis.CategoryViewSet)
router.register(r'orders', apis.OrderViewSet)
router.register(r'todos', apis.TodoViewSet)
router.register(r'users', apis.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', todo.index, name='index'),

    # rest framework
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
