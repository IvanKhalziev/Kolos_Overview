from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
