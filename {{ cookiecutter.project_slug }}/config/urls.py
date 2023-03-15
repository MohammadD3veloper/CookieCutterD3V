"""{{ cookiecutter.project_slug }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

{%- if cookiecutter.api_framework == "GrapheneDjango" %}
from graphene_django.views import GraphQLView
{%- elif cookiecutter.api_framework == "RestFramework" %}
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
{%- endif %}


urlpatterns = [
    path('{{ cookiecutter.project_slug }}/SecurePanel/ui/', admin.site.urls),
    {%- if cookiecutter.api_framework == "RestFramework" %}
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api-auth/', include('rest_framework.urls')),
    {%- elif cookiecutter.api_framework == "GrapheneDjango" %}
    path("graphql/", GraphQLView.as_view(graphiql=True)),
    {%- endif %}
    {%- if cookiecutter.use_prometheus != "n" %}
    path('prometheus/', include('django_prometheus.urls')),
    {%- endif %}    
]
