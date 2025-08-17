from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCreateForm


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            "form": create_form
        }
        return render(request=request, template_name="users/register.html", context=context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect("users:login")
        else:
            context = {
                "form": create_form
            }
            return render(request=request, template_name="users/register.html", context=context)

class LoginView(View):
    def get(self, request):
        return render(request=request, template_name="users/login.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request=request, user=user)
            return redirect(to="landing_page")
        else:
            context = {
                "login_form": login_form
            }
            return render(request=request, template_name="users/login.html", context=context)
