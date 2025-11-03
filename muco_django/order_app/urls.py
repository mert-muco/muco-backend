from django.urls import path
from .views import StripeCheckoutView, OrderView, SelectedOrderView

urlpatterns = [
    path('', OrderView.as_view()),
    path('id/', SelectedOrderView.as_view()),
    path('checkout/', StripeCheckoutView.as_view())
]