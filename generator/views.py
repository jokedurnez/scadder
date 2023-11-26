from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import KeyChainInput
from .forms import KeyChainInputForm
import datetime

def about(request):
    template = loader.get_template("generator/about.html")
    return HttpResponse(template.render({}, request))


def index(request):
    context = {
        "my_text": "this is some text I want to display"
    }
    template = loader.get_template("generator/index.html")
    return HttpResponse(template.render(context, request))

def generator(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = KeyChainInputForm(request.POST)
        if form.is_valid():
            input = KeyChainInput(
                name = form.cleaned_data['name'],
                date = datetime.datetime.now()
            )
            input.save()
            template = loader.get_template("generator/index.html")
            context = {
                "my_text": "successsss"
            }
            return HttpResponse(template.render(context, request))
            
    form = KeyChainInputForm()
    context =  {"form": form}
    template = loader.get_template("generator/generator.html")
    # return HttpResponse(template, render(context, request))
    return render(request, "generator/generator.html", {"form": form})
