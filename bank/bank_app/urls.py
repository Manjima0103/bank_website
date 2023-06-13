from django.urls import path
from . import views

app_name = 'bank_app'

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("branches/", views.branches, name="branches"),
    path("branches/<str:district>/", views.district_wikipedia, name="district_wikipedia"),
    path("new_page/", views.new_page, name="new_page"),
    path("form_submission/", views.form_submission, name="form_submission"),

    path("logout/", views.logout, name="logout"),
]
