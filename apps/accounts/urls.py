from django.urls import path, include
from apps.accounts.Api.urls import router_users
from apps.accounts.views import ListAll

urlpatterns = [
    path('list/', ListAll.as_view(), name='list_all'),
    path('user/', include(router_users))
]
