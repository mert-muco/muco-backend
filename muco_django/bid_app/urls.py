from django.urls import path
from .views import BidsView, BidView, CreateBidView

urlpatterns = [
    path('', BidView.as_view()),
    path('preview/', BidsView.as_view()),
    path('create/', CreateBidView.as_view())
]