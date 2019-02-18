from django.contrib.auth.models import User
from authentication.models import Profile
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers import ProfileSerializer, UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer
