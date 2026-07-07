from django.urls import path

from .views import home

from .views import login_view

from .views import logout_view

from .views import dashboard

urlpatterns = [

    path(
        "",
        home,
        name="home"
    ),

    path(
        "login/",
        login_view,
        name="login"
    ),

    path(
        "logout/",
        logout_view,
        name="logout"
    ),

    path(
        "dashboard/",
        dashboard,
        name="dashboard"
    ),

]