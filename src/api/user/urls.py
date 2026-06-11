from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.user.views import event_views, register_views

router = DefaultRouter()
router.include_root_view = False

urlpatterns = [
    path('event/', event_views.EventApiView.as_view(), name='event'),
    path('registration/', register_views.RegistrationApiView.as_view(), name='registration'),

    # path('', include(router.urls)),
    # path('restaurant/', RestaurantViewset.as_view({'get': 'list','post':'create'}), name='restaurant-detail'),
]

