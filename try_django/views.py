from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .form import ContactForm
from blog.models import BlogPost


def home_page(request):
    query = BlogPost.objects.all()[:5]
    context = {"title": "Welcome to TRY DJANGO", "blog_list": query}
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
