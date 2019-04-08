from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):

	if request.method == "POST":

		username = request.POST['username']

		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if not user is None:

			login(request, user)

			return redirect('auth_app:login_success_view')

	return render(request,'auth_app/login.html')

def logout_view(request):

	if request.method == "POST":

		logout(request)

		return redirect('auth_app:login_view')
		
	return render(request,'auth_app/login.html')

def login_success(request):
	return render(request,'auth_app/success.html')