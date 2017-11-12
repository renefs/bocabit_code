from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, generic.TemplateView):
    # Login mixin
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    # template view
    template_name = 'index.html'
