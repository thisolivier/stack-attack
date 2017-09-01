from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'register$', views.process_reg),
    url(r'login$', views.process_login),
    url(r'logout$', views.process_logout),
    url(r'^', views.render_portal),
]