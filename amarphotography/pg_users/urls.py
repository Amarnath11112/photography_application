from django.urls import path
from .views import signup, home, signup_page, login_page, login
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("home/", home, name="home"),
    path("signup_page/", signup_page, name="signup_page"),
    path("login_page/", login_page, name="login_page"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

