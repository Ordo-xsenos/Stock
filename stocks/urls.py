from django.urls import path
from .views import home
from .api import api_search,api_quote

urlpatterns = [
    path('', home, name='home'),
    path('search/<str:query>/', api_search),
    path('quote/<str:symbol>/', api_quote),
]