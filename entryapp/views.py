from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import PaymentForm
from .models import PaymentEntry


def index(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = PaymentForm()
        return render(request, "entryapp/index.html", {"form": form})

