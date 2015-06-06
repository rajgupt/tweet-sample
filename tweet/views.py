from django.shortcuts import render
from django.shortcuts import get_object_or_404, Http404
from django.http import HttpResponseRedirect, HttpResponse

from django.views import generic

from .models import message, handle
 

# Create your views here.
class IndexView(generic.ListView):
    template_name = "tweet/index.html"
    model = handle
    context_object_name = "user_list"

class UserView(generic.DetailView):
    template_name = "tweet/user.html"
    model = handle
