import logging

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from codeapp.models import Code, Snippet

logger = logging.getLogger('webapp.codeapp')


class CodeIndexView(LoginRequiredMixin, generic.ListView):
    # Login mixin
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'code_list'
    # template view
    template_name = 'code/code_list.html'

    def get_queryset(self):
        """

        :return: Codes only from the user
        """
        return Code.objects.filter(owner=self.request.user)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(CodeIndexView, self).get_context_data(**kwargs)
    #     context['markets_list'] = Market.objects.all()
    #     return context


class CodeCreateView(generic.CreateView):
    model = Code
    fields = ['title', 'description']
    success_url = reverse_lazy('codeapp:code_list')
    template_name = 'code/code_form.html'

    def __init__(self, **kwargs):
        self.object = None
        super().__init__(**kwargs)

    def form_valid(self, form, **kwargs):
        logger.debug("Form is valid")

        self.object = form.save(commit=False)
        self.object.owner = self.request.user

        form_data = form.cleaned_data
        logger.debug(form_data)

        self.object.save()

        return super(CodeCreateView, self).form_valid(form)


class CodeDetailView(generic.DetailView):
    model = Code
    template_name = 'code/code_detail.html'
    # pk_url_kwarg = 'code_id'


class SnippetCreateView(generic.CreateView):
    model = Snippet
    fields = ['title', 'language', 'text']
    template_name = 'snippet/snippet_form.html'
    # pk_url_kwarg = 'code_id'

    def get_queryset(self):
        """Return the last five published questions."""
        logger.debug(self.request)
        pk = self.kwargs.get('pk')
        return Code.objects.get(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['code'] = Code.objects.get(pk=pk)
        return context

    # def __init__(self, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     self.code = Code.objects.get(pk=pk)
    #     super().__init__(**kwargs)
