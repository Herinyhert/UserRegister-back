from rest_framework.routers import DefaultRouter
from apps.accounts.Api.views import UserApiViewSet

router_users = DefaultRouter
router_users.register(prefix='user', basename='user', viewset=UserApiViewSet)