from rest_framework import routers
from homepage import api_views

router = routers.DefaultRouter()
router.register(r'users', api_views.ExampleUsersViewset)
router.register(r'citations', api_views.ExampleCitationsViewset)