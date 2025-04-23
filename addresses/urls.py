from django.urls import path
from .views import AddressCreateView, RiskCheckView

urlpatterns = [
    path('addresses/', AddressCreateView.as_view()),
    path('addresses/<int:id>/risks/', RiskCheckView.as_view()),
]
