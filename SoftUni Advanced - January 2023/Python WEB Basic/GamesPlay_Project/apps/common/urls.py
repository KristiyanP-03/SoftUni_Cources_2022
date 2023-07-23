from django.urls import path, include

from apps.common.views import home_page, dashboard

urlpatterns = [
    path("", home_page, name="home_page"),
    path("dashboard/", dashboard, name="dashboard")
]