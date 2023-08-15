from rest_framework import generics
from ..models.users import User
from ..serializers.users import UserSerializer

class ActiveUsersListView(generics.ListAPIView):
    queryset = User.objects.filter(active=True)
    serializer_class = UserSerializer
