from rest_framework.routers import SimpleRouter

from src.users.views import UserViewSet, UserCreateViewSet

usersRouter = SimpleRouter()

usersRouter.register(r'users', UserViewSet)
usersRouter.register(r'users', UserCreateViewSet)
