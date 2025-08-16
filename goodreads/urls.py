from django.contrib import admin
from django.urls import path, include

from goodreads.views import landing_page

urlpatterns = [
    path('', landing_page, name="landing_page"),
    path(route="users/", view=include("users.urls"),),
    path('admin/', admin.site.urls),
]
