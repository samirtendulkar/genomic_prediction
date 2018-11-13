from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

router = DefaultRouter()

router.register("login", views.LoginViewSet, base_name="login")
router.register("patient", views.PatientsApiView)
router.register("embryo", views.EmbroApiView)


urlpatterns =[
   path('', include(router.urls)),
   path('patient/<int:pk>/show_pdf', views.generate_pdf, name='show_pdf')
]

