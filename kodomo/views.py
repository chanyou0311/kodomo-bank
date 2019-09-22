from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.http.response import JsonResponse
from django.urls import reverse_lazy

from .models import Ticket, Bank, User, Style, Value
from .forms import QRCodeForm


class HomeTemplateView(TemplateView):
    template_name = "kodomo/home.html"


class TicketListView(ListView):
    template_name = "kodomo/tickets/list.html"
    model = Ticket


class UseTicketView(FormView):
    template_name = "kodomo/tickets/use.html"
    form_class = QRCodeForm
    success_url = reverse_lazy('kodomo:tickets_use_done')

    def form_valid(self, form):
        print("hogehoge")
        bank = Bank.objects.get(pk=1)
        bank.balance = bank.balance + 10
        bank.save()
        ticket = Ticket.objects.filter(is_active=True).first()
        if ticket is not None:
            ticket.is_active = False
            ticket.save()
        return super().form_valid(form)


class UseDoneTicketView(TemplateView):
    template_name = "kodomo/tickets/use_done.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket = Ticket.objects.filter(is_active=False).last()
        context["latest_ticket"] = ticket
        context["user"] = User.objects.first()
        return context


class BuyTicketView(TemplateView):
    template_name = "kodomo/tickets/buy.html"

    def post(self, request, *args, **kwargs):
        self.request["POST"]
        return render(request, self.template_name)


class BuyAskTicketView(TemplateView):
    template_name = "kodomo/tickets/buy_ask.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = User.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        self.request["POST"]
        return render(request, self.template_name)


class BankDetailView(DetailView):
    template_name = "kodomo/banks/detail.html"
    model = Bank


def bank_balance_api(request, pk):
    bank = Bank.objects.get(pk=pk)
    d = {"balance": bank.balance}
    return JsonResponse(d)


def tickets_buy_process(request, price):
    user = User.objects.first()
    value = Value.objects.filter(price=price).first()
    if value is None:
        value = Value.objects.create(price=price, cost=2)
    style = Style.objects.first()

    tickets = [Ticket(user=user, value=value, style=style) for i in range(10)]
    Ticket.objects.bulk_create(tickets)

    bank = Bank.objects.get(pk=1)
    bank.balance = bank.balance - 20
    bank.save()
    return redirect(reverse("kodomo:tickets_list"))
