from django.urls import path, include

urlpatterns = [
    path("auth/", include("solidaire_api.auth.urls")),
    path("post/", include("solidaire_api.post.urls")),
    # path("comments/", include("solidaire_api.comment.urls")),
]