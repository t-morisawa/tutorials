from django.shortcuts import render
from django.http.response import HttpResponse
from app.form import ContactForm


data = {'subject': 'hello',
        'age': 21,
        'hoge': 'fuga'
}


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # 中略
    else:
        form = ContactForm(request.GET)
    params={
        'form': form,
    }
    return render(request, 'index.html', params)
