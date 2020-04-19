from django.urls import path
from .views import home, customer, product
app_name='accounts'
urlpatterns = [
    path('',home, name='home'),
    path('customer/', customer, name='customer'),
    path('product/', product, name='product'),
]