from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupview.as_view(), name='signup'),
    path('shifts/', views.ShiftListOrCreate.as_view(), name='shifts'),
]