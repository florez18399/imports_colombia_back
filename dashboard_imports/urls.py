from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'countries', views.ContriesView, basename='countries')
router.register(r'aduanas', views.AduanasView, basename='aduanas')
router.register(r'imports', views.ImportsProcessViewSet, basename='imports')
router.register(r'by_pro_country', views.ImportsProcessByProCountryViewSet, basename='by_pro_country')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]