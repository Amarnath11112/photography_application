from django.urls import path
from .views import about,contact,home,stories,films
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("stories/", stories, name="stories"),
    path("films/", films, name="films"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

