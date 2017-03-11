from django.conf.urls import url, include
from rest_framework import routers
from jobs import views

router = routers.DefaultRouter()
router.register(r'jobs', views.JobViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'location', views.LocationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]