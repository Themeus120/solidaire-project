from django.urls import path, include

urlpatterns = [
    path("token/", include("solidaire_api.auth.token.urls")),
]