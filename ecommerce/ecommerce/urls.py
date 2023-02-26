from django.contrib import admin
from django.urls import path
from users.views import user_api_view
from users.views import one_user_api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get/', user_api_view,name='Users view API'),
    path('api/get/<int:pk>', one_user_api_view, name='One user api view'),
]
