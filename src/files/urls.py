from rest_framework.routers import SimpleRouter

from .views import FilesViewset

files_router = SimpleRouter()

files_router.register(r'files', FilesViewset)
