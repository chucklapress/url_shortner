from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here
from django.views.generic import View, TemplateView, CreateView
from django.http import HttpResponse
from urlbook.models import BookMark


class IndexView(View):

    def get(self, request):
        return HttpResponse("Welcome")


class NewTemplateView(TemplateView):
    template_name = "new_template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[""] = ""
        context["url"] = BookMark.objects.all()
        return context

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'