from django.urls import path
from . import views

urlpatterns = [
    #api endpoint to signup, takes email, password and password confirm as json input in post request to create user
    path('SignUp/', views.signupview.as_view(), name='signup'),
    #api endpoint to view all shifts created(GET) or to create a new shift(POST) only for logged in users.
    path('Shifts/', views.ShiftListOrCreate.as_view(), name='shifts'),
]