from rest_framework.routers import DefaultRouter
from .views import MyUtils

router = DefaultRouter(trailing_slash=False)
router.register('SolServerTest', MyUtils, basename='hello')

urlpatterns = router.urls