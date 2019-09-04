from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view
from .users.views import UserViewSet, UserCreateViewSet
from .files.views import MyFileView

schema_view = get_swagger_view(title='Pastebin API')

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),

    # auth
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),

    # api
    path('api/v1/', include(router.urls)),
    url(r'^api/v1/password_reset/',
        include('django_rest_passwordreset.urls', namespace='password_reset')),

    # file upload
    url(r'^api/v1/file/upload/$', MyFileView.as_view(), name='file-upload'),

    # swagger docs
    url(r'^swagger$', schema_view),

    # the 'api-root' from django rest-frameworks default router
    re_path(
        r'^$',
        RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
