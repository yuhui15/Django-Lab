from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.editor, name="add"),
    path("save/", views.save_page, name="save"),
    path("page/<int:id>/", views.view_page, name="view"),
    path("page/<int:id>/like/", views.add_like, name="like"),
    path("page/<int:id>/likes/", views.view_likes, name="likes"),
]
