from django.urls import path

from .views import home_page_view, AboutPageView, ProductsView #NEW

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),  # About page
    path("", home_page_view, name="home"),  # Home page
    path("products/", ProductsView.as_view(), name="products"),  # Products page
]