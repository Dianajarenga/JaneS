from .views import bluehaven_list, bluehaven_profile, delete_bluehaven, edit_bluehaven, register_bluehaven
from django.urls import path

urlpatterns=[
    path("register/",register_bluehaven,name="register_bluehaven"),
    path("list/",bluehaven_list,name="bluehaven_list"),
    path("edit/<int:id>/",edit_bluehaven,name="edit_bluehaven"),
    path("profile/<int:id>/",bluehaven_profile,name="bluehaven_profile"),
    path("delete/<int:id>/",delete_bluehaven,name="delete_bluehaven")  
]