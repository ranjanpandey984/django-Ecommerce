from django.urls import path, include
from rest_framework import routers
from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'item', ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('filter_items/', ItemFilterView.as_view(), name= 'filter_items'),
    path('item_detail/<int:pk>', ItemDetailView.as_view(), name= 'item_detail')
]