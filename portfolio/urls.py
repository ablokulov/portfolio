from django.urls import path
from .views import PortfolioViews

urlpatterns = [
    path('portfolio/', PortfolioViews.as_view(), name='portfolio'),
]
