from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'countries', views.ContriesView, basename='countries')
router.register(r'imports', views.ImportsProcessViewSet, basename='imports')
router.register(r'by_pro_country', views.ImportsProcessByProCountryViewSet, basename='importsByProCountry')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]