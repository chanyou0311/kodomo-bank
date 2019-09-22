from django.urls import path

from . import views


app_name = "kodomo"
urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path("tickets/", views.TicketListView.as_view(), name="tickets_list"),
    path("banks/", views.BankDetailView.as_view(), name="banks_detail"),
]

