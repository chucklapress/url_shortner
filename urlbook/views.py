from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here
from django.views.generic import View, ListView, CreateView, TemplateView
from django.http import HttpResponse
from urlbook.models import BookMark, Click


class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class NewListView(ListView):
    model = BookMark



class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'

class CreateBookMarkView(CreateView):
    model = BookMark
    fields = ['url','title','description','uniqueid','appuser']
    success_url = '/'

class ClickListView(ListView):
    model = Click
