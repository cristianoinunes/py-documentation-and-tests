from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from cinema.views import OrderViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Cinema API",
        default_version="v1",
        description="Documentação da API do sistema de cinema",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@cinema.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
    path("api/user/", include("user.urls", namespace="user")),
    path("__debug__/", include("debug_toolbar.urls")),

    path("swagger/",
         schema_view.with_ui("swagger", cache_timeout=0),
         name="swagger-ui"),
    path("api/token/",
         TokenObtainPairView.as_view(),
         name="token_obtain_pair"),
    path("api/token/refresh/",
         TokenRefreshView.as_view(),
         name="token_refresh"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
