from django.urls import path

from . import views


app_name = "kodomo"
urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path("tickets/", views.TicketListView.as_view(), name="tickets_list"),
    path("tickets/use/", views.UseTicketView.as_view(), name="tickets_use"),
    path("tickets/use-done", views.UseDoneTicketView.as_view(), name="tickets_use_done"),
    path("tickets/buy/", views.BuyTicketView.as_view(), name="tickets_buy"),
    path("tickets/buy-ask/<int:price>", views.BuyAskTicketView.as_view(), name="tickets_buy_ask"),
    path("banks/<int:pk>/balance/", views.bank_balance_api, name="bank_balance_api"),
    path("banks/<int:pk>/", views.BankDetailView.as_view(), name="banks_detail"),
]
