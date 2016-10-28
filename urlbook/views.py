from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView, CreateView, TemplateView, UpdateView, DeleteView, DetailView, RedirectView
from django.http import HttpResponse
from urlbook.models import BookMark, Click
from django.core.urlresolvers import reverse_lazy
from hashids import Hashids





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


class BookMarkListView(ListView):
    model = BookMark


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/'


from django.contrib.auth.mixins import LoginRequiredMixin
class CreateBookMarkView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = BookMark
    fields = ['url','title','description','hashid','appuser']
    success_url = '/'
    def form_valid(self, form):
        hashids = Hashids(salt="donkeykongruleslwhisper")
        bookmark = form.save(commit=False)
        bookmark.hashid = hashids.encode(id(bookmark.url))
        bookmark.user = self.request.user
        form.instance.created_by = self.request.user
        return super(CreateBookMarkView, self).form_valid(form)

class BookMarkDetailView(DetailView):
    model = BookMark



class BookMarkUpdateView(UpdateView):
    model = BookMark
    success_url = '/mybookmarks/'
    fields = ['url','title','description','uniqueid','appuser']
    template_name_suffix = '_update_form'


class BookMarkDeleteView(DeleteView):
    model = BookMark
    success_url = '/mybookmarks/'
    template_name = "delete_bookmark.html"
    fields = ['url', 'title','description','uniqueid','appuser']


class ClickListView(ListView):
    model = Click


from django.contrib.auth.mixins import LoginRequiredMixin
class MyBookMarkView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = "my_bookmarks.html"
    model = BookMark
    def get_queryset(self):
        return BookMark.objects.filter(appuser=self.request.user)
    class Meta:
        ordering = ['-created']

class DisplayClickRedirectView(RedirectView):

    def get(self, request, *args, **kwargs):
        hash_id = self.kwargs.get('hashid', None)
        link = BookMark.objects.get(hashid=hash_id)
        self.url = link.url
        link.click_count += 1
        link.save()
        Click.objects.create(url=link, timestamp=datetime.datetime.now())
        return super(DisplayClickRedirectView, self).get(request, *args, **kwargs)
