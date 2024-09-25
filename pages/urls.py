from django.urls import path

from .views import home_page_view, AboutPageView #NEW

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"), #NEW
    path("", home_page_view, name="home"), #NEW
]