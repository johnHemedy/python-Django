from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .form import ContactForm


def home_page(request):
    my_title = "Hello there..."
    context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    return render(request, "home.html", context)


def about_page(request):
    context = {"title": "About us"}
    return render(request, "about.html", context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = ContactForm()
    context = {"title": "Contact us", "form": form}
    return render(request, "form.html", context)


def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_object = get_template(template_name)
    return HttpResponse(template_object.render(context))
