from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import UserViewSet, AddressViewSet
from products.views import ProductViewSet, OrderViewSet
from wallets.views import WalletViewSet, PaymentViewSet, CardViewSet

router = routers.DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'wallets', WalletViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'cards', CardViewSet)
router.register(r'orders', OrderViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
