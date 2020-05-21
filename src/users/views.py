from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from src.users.models import User
from src.users.permissions import IsUserOrReadOnly
from src.users.serializers import CreateUserSerializer, UserSerializer


class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly, )

    @action(detail=False, methods=['get'], url_path='me', url_name='me')
    def get_user_data(self, instance):
        try:
            return Response(UserSerializer(self.request.user, context={'request': self.request}).data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e.__dict__)
            return Response({'error': 'Wrong auth token' + e}, status=status.HTTP_400_BAD_REQUEST)


class UserCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny, )
