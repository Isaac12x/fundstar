from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from information import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.render_html, name="index"),
    url(r'^successful-entrepreneur/$', views.onboard_successful_entrepreneur,
        name="founder"),
    url(r'^angel/$', views.onboard_angel, name="angel"),
    url(r'^entrepreneur/$', views.onboard_entrepreneur, name="entrepreneur"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
