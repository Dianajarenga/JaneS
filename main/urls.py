
from django.urls import path
from .  import views

app_name = "main" 



urlpatterns = [
       
        path("home", views.homepage, name="homepage"),
        path("land", views.landingpage, name="landingpage"),

        path("password_reset", views.password_reset_request, name="password_reset"),
        path("register", views.register_request, name="register"),
        path("login", views.login_request, name="login"),
        path("logout", views.login_request, name="logout"),

        path("contact", views.contact, name="contact"),
        path("investment", views.investment, name="investment"),
        path("list/add",views.register_investment,name="register_investment"),
        path("add",views.register_investment,name="register_investment"),

        path("list/investment",views.investment_list,name="investment_list"),
        path("edit/<int:id>/",views.edit_investment,name="edit_investment"),
        path("profile/<int:id>/",views.investment_profile,name="investment_profile"),
        path("delete/<int:id>", views.delete_investment,name="delete_investment")

]
