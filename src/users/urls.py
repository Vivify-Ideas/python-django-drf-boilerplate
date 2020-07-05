from rest_framework.routers import SimpleRouter

from src.users.views import UserViewSet

usersRouter = SimpleRouter()

usersRouter.register(r'users', UserViewSet)
