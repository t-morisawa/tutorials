from django.shortcuts import render
from django.http.response import HttpResponse
from app.form import ContactForm, MultiForm


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm(request.GET)
    params={
        'form': form,
    }
    return render(request, 'index.html', params)


def formset(request):
    if request.method == 'POST':
        form = MultiForm(request.POST)
    else:
        form = MultiForm(request.GET)
    params={
        'form': form,
    }
    return render(request, 'formset.html', params)
