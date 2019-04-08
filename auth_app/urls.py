from django.urls import path
from . import views

app_name="auth_app"

urlpatterns = [

	path('login/', views.login_view, name="login_view"),
	path('logout/', views.logout_view, name="logout_view"),
	path('success/', views.login_success, name="login_success_view"),

]