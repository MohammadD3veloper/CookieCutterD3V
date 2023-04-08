from django.urls import path
from rest_framework.routers import SimpleRouter

{%- if cookiecutter.api_framework != "BasicHTML" %}
from apis.authentication_api import AuthenticationViewSet


router = SimpleRouter()
router.register(r'', AuthenticationViewSet.as_view(), basename="authentication")


urlpatterns = [
    path(r'', router.urls)
]

{%- else %}
from .views import Login

urlpatterns = [
    path(r'login/', Login.as_view(), name="login")
]

{%- endif %}