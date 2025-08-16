from django.urls import path

from users.views import RegisterView, LoginView

app_name = "users"

urlpatterns = [
    path(route="register", view=RegisterView.as_view(), name="register"),
    path(route="login", view=LoginView.as_view(), name="login"),
]
