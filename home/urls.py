from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('product_details/<slug>', ProductDetailView.as_view(), name='product_details'),
    path('product_review', product_review, name='product_review'),
]
