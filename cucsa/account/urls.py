from django.urls import path
from cuser.forms import AuthenticationForm
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name="account/login.html", 
												authentication_form=AuthenticationForm),
												name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name="logout"),
	path('signup/', views.SignUp.as_view(), name="signup"),
]
