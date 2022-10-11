from django.urls import path
from . import views


urlpatterns = [
    path("api/", views.urlshortener, name="show_urls"),
    path("api/<shortened_part>", views.redirect_url_view),
    path("api/create_user/", views.create_user),
    path("api/login_user/", views.login_user),
    path("api/logout_user/", views.logout_user),
    path("api/login_state/", views.login_state),
    path("api/urls_detail/", views.get_urlshortener_registerd),
    path("api/specific_url_detail/<shortened_part>", views.specific_url_detail)
]
