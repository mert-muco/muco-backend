from django.urls import path
from .views import OrderView, SelectedOrderView

urlpatterns = [
    path('', OrderView.as_view()),
    path('id/', SelectedOrderView.as_view())
]