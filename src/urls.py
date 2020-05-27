from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from src.files.views import MyFileView
from src.social.views import exchange_token, complete_twitter_login
from src.users.urls import usersRouter

schema_view = get_schema_view(
    openapi.Info(title="Pastebin API", default_version='v1'),
    public=True,
)

router = DefaultRouter()

router.registry.extend(usersRouter.registry)

urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),

    # summernote editor
    path('summernote/', include('django_summernote.urls')),

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


    # social login
    url('', include('social_django.urls', namespace='social')),
    url(r'^complete/twitter/', complete_twitter_login),
    url(r'^api/v1/social/(?P<backend>[^/]+)/$', exchange_token),

    # swagger docs
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # the 'api-root' from django rest-frameworks default router
    re_path(
        r'^$',
        RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
