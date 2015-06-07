from django.shortcuts import render
from django.shortcuts import get_object_or_404, Http404
from django.http import HttpResponseRedirect, HttpResponse

from django.views import generic

from .forms import TweetForm
from .models import message, handle
 

# Create your views here.
class IndexView(generic.ListView):
    template_name = "tweet/index.html"
    model = handle
    context_object_name = "user_list"

class UserView(generic.DetailView):
    template_name = "tweet/user.html"
    model = handle

class CreateView(generic.edit.FormView):
    template_name = "tweet/tweet_form.html"
    form_class = TweetForm
    success_url = "/"
    def form_valid(self, form):
        user, is_created = handle.objects.get_or_create(value=form.cleaned_data['user'])
        user.message_set.create(value=form.cleaned_data['message'])
#         print(user)
        return super(CreateView, self).form_valid(form)