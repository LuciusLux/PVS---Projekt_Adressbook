from rest_framework import routers
from .views import ContactApiView, AddressApiView

router = routers.DefaultRouter()
router.register('contacts', ContactApiView)
router.register('addresses', AddressApiView)

urlpatterns = router.urls