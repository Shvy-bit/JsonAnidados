from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Sales.views import SaleWithDetailsViewSet

router = routers.DefaultRouter()
router.register(r'sales', SaleWithDetailsViewSet, basename='sale')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restful/', include(router.urls)),
]