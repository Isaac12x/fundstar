from django.shortcuts import render
from information.forms import Onboard_Serial, Onboard_Angel
from django.template.context_processors import csrf
from django.contrib import messages
from information.models import Angel, SerialEntrepreneur

# Create your views here.
def render_html(request):
    if request.path == "/":
        return render(request, 'fundstar.html')


def onboard_successful_entrepreneur(request):
    form = Onboard_Serial(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Thank you very much for helping us here! We'll check everything as fast as thunder and get back to you :)")

    context = {
        'title': "Onboard Successful Entrepreneur",
        'form': form,
    }

    # return render(request, 'serial-entrepreneur.html', context)
    return render(request, 'sentrepreneurtemp.html')


def onboard_angel(request):
    form = Onboard_Angel(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Thank you very much, we will be in touch soon")

    context = {
        'title': 'Onboard Angel',
        'form': form,
    }
    # return render(request, 'angel.html', context)
    return render(request, 'angeltemp.html')


def onboard_entrepreneur(request):
    pass
