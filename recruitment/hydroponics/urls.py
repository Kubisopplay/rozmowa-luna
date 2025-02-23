from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from hydroponics.views import HydroponicSystemListCreateView, HydroponicSystemDetailView, MeasurementListCreateView, MeasurementDetailView, recent_measurements
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Hydroponic System API",
        default_version='v1',
        description="API documentation for the Hydroponic System project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[JWTAuthentication],
    
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Add the admin site path
    path('hydroponic-systems/', HydroponicSystemListCreateView.as_view(), name='hydroponic-system-list-create'),
    path('hydroponic-systems/<int:pk>/', HydroponicSystemDetailView.as_view(), name='hydroponic-system-detail'),
    path('hydroponic-systems/<int:pk>/recent-measurements/', recent_measurements, name='recent-measurements'),
    path('measurements/', MeasurementListCreateView.as_view(), name='measurement-list-create'),
    path('measurements/<int:pk>/', MeasurementDetailView.as_view(), name='measurement-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
