from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from addresses.views import AddressViewSet
from users.views import UserViewSet
from users_addresses.views import UserAddressViewSet
from products.views import ProductViewSet
from wallets.views import WalletViewSet
from payments.views import PaymentViewSet 
from cards.views import CardViewSet
from orders.views import OrderViewSet
from products_orders.views import ProductOrderViewSet

router = routers.DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'users', UserViewSet)
router.register(r'users_addresses', UserAddressViewSet)
router.register(r'products', ProductViewSet)
router.register(r'wallets', WalletViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'cards', CardViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'products_orders', ProductOrderViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
