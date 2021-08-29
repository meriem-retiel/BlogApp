



from django.urls.conf import path
from .views import PostViewset, UserViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('user',UserViewset, basename='users')
router.register('',PostViewset,basename='posts')

urlpatterns = router.urls