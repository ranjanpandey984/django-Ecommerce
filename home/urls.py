from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('subcategory/<slug>', SubCategoryViews.as_view(), name = 'subcategory'),
    path('brand/<slug>', BrandViews.as_view(), name = 'brand'),
]
