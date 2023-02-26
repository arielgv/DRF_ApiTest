from django.contrib import admin
from django.urls import path
from users.views import user_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get/', user_api_view,name='Users view API'),
]
