from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.http.response import JsonResponse
from django.urls import reverse_lazy

from .models import Ticket, Bank
from .forms import QRCodeForm


class HomeTemplateView(TemplateView):
    template_name = "kodomo/home.html"


class TicketListView(ListView):
    template_name = "kodomo/tickets/list.html"
    model = Ticket


class UseTicketView(FormView):
    template_name = "kodomo/tickets/use.html"
    form_class = QRCodeForm
    success_url = reverse_lazy('kodomo:tickets_use')

    def form_valid(self, form):
        print("hogehoge")
        bank = Bank.objects.get(pk=1)
        bank.balance = bank.balance - 10
        bank.save()
        return super().form_valid(form)


class UseDoneTicketView(TemplateView):
    template_name = "kodomo/tickets/use_done.html"


class BuyTicketView(TemplateView):
    template_name = "kodomo/tickets/buy.html"

    def post(self, request, *args, **kwargs):
        self.request["POST"]
        return render(request, self.template_name)


class BuyAskTicketView(TemplateView):
    template_name = "kodomo/tickets/buy_ask.html"


def bank_balance_api(request, pk):
    bank = Bank.objects.get(pk=pk)
    d = {"balance": bank.balance}
    return JsonResponse(d)


# class BankView(Detail):
#     template_name = "kodomo/banks/detail.html"

