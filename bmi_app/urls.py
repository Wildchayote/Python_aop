from django.urls import path
from bmi_app.views import calculate_bmi, bmi_result

urlpatterns = [
    path('calculate/', calculate_bmi, name='calculate_bmi'),
    path('result/<int:pk>/', bmi_result, name='bmi_result'),
]

