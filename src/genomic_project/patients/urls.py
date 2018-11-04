from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("login", views.LoginViewSet, base_name="login")
router.register("patient", views.PatientsApiView)
router.register("embryo", views.EmbroApiView)

urlpatterns = [
    url(r'', include(router.urls))
]
