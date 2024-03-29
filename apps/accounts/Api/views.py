from rest_framework.viewsets import ModelViewSet
from apps.accounts.models import User
from apps.accounts.Api.serializers import UserSerializer

class UserApiViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()