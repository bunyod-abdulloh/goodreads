from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class RegisterView(View):
    def get(self, request):
        return render(request=request, template_name="users/register.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        # passwordni hashlash uchun
        user.set_password(raw_password=password)
        user.save()

        return redirect("users:login")


class LoginView(View):
    def get(self, request):
        return render(request=request, template_name="users/login.html")
