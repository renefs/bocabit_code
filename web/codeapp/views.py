import logging

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin

from codeapp.models import Code, Snippet

logger = logging.getLogger('webapp.codeapp')


class CodeIndexView(LoginRequiredMixin, generic.ListView):
    # Login mixin
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'code_list'
    # template view
    template_name = 'code/code_list.html'
    paginate_by = 10

    def get_queryset(self):
        """

        :return: Codes only from the user
        """
        return Code.objects.filter(owner=self.request.user)


class CodeCreateView(LoginRequiredMixin, generic.CreateView):
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


class CodeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Code
    template_name = 'code/code_detail.html'


class CodeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Code
    fields = ['title', 'description']
    template_name = 'code/code_form_update.html'

    def get_success_url(self):
        return reverse_lazy('codeapp:code_detail', kwargs={'pk': self.object.id})


class SnippetContextMixin(LoginRequiredMixin, ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code_pk = self.kwargs.get('code_id')
        context['code'] = Code.objects.get(pk=code_pk)
        return context


class SnippetCreateView(generic.CreateView, SnippetContextMixin):
    model = Snippet
    fields = ['title', 'language', 'text']
    template_name = 'snippet/snippet_form.html'

    def __init__(self, **kwargs):
        self.object = None
        super().__init__(**kwargs)

    def get_queryset(self):
        logger.debug(self.request)
        pk = self.kwargs.get('pk')
        return Code.objects.get(pk=pk)

    def form_valid(self, form, **kwargs):
        logger.debug("Form is valid")
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        code_pk = self.kwargs.get('pk')
        self.object.code = Code.objects.get(pk=code_pk)
        self.object.save()

        return super(SnippetCreateView, self).form_valid(form)


class SnippetDetailView(generic.DetailView, SnippetContextMixin):
    model = Snippet
    template_name = 'snippet/snippet_detail.html'


class SnippetUpdateView(generic.UpdateView, SnippetContextMixin):
    model = Snippet
    fields = ['title', 'language', 'text']
    template_name = 'snippet/snippet_form_update.html'
