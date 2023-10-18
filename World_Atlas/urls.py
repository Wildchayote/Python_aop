from django.urls import path
from World_Atlas.views import country_form, get_capital

urlpatterns = [
    path('country/', country_form, name = 'country_form'),
    path('result/<int:pk>/', get_capital, name = 'get_capital')
]
