from rest_framework.routers import SimpleRouter

from src.users.views import UserViewSet, AnalysisView

users_router = SimpleRouter()

users_router.register(r'users', UserViewSet)
users_router.register(r'analyst',AnalysisView)

