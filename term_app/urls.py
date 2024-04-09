from django.contrib import admin
from django.urls import path, include

from term_app import views

urlpatterns = [
    path("",views.index,name="index"),
    # path("homepage", views.homepage, name="homepage"),
    path("about",views.about,name="about"),
    path("add_employee",views.add_employee,name="add_employee"),
    path("view",views.view,name="view"),
    path("delete_data/<int:id>/", views.delete_data, name="delete_data"),
    path("update_data/<int:id>/", views.update_data, name="update_data")

]
