from django.shortcuts import render
from valid.forms import *
# Create your views here.


def index(request):
    if request.POST:

        form = ProductForm(request.POST or None)

        if form.is_valid():
            form.save()
            return render(request, 'valid/success.html')
        else:
            return render(request, 'valid/index.html', {'form': form})
    else:
        form = ProductForm()
        return render(request, 'valid/index.html', {'form': form})

