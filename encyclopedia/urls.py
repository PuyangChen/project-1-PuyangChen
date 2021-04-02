from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>",views.show, name="show"),
    path("search/",views.search,name="search"),
    path("no_match",views.no_match, name="no_match"),
    path("new_entry/",views.new_entry,name="new_entry"),
    path("create/",views.create,name="create"),
    path("random_page/",views.random_page,name="random_page"),
    path("edit_entry/<str:title>",views.edit_entry,name="edit_entry"),
    path("save_entry/",views.save_entry,name="save_entry")
]
