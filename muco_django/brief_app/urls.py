from django.urls import path
from .views import TopBriefsView, BriefView, BrowseView, CompanyBriefs, CreateBreifView

urlpatterns = [
    path('', BriefView.as_view()),
    path('browse/', BrowseView.as_view()),
    path('top_briefs/', TopBriefsView.as_view()),
    path('company/', CompanyBriefs.as_view()),
    path('create/', CreateBreifView.as_view())
]