import logging

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import ContextMixin

from codeapp.models import Code, Snippet, Tag

logger = logging.getLogger('webapp.codeapp')


class AppContextMixin(LoginRequiredMixin, ContextMixin):
    context_type = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = self.context_type
        return context


#
# CODE
#
class CodeContextMixin(AppContextMixin):
    context_type = "code"


#
# TAG
#
class TagContextMixin(AppContextMixin):
    CONTEXT_TYPE = "tag"


class CodeIndexView(generic.ListView, CodeContextMixin):
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


class CodeCreateView(generic.CreateView, CodeContextMixin):
    model = Code
    fields = ['title', 'description', 'tags']
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


class CodeDetailView(generic.DetailView, CodeContextMixin):
    model = Code
    template_name = 'code/code_detail.html'


class CodeUpdateView(generic.UpdateView, CodeContextMixin):
    model = Code
    fields = ['title', 'description', 'tags']
    template_name = 'code/code_form_update.html'

    def get_success_url(self):
        return reverse_lazy('codeapp:code_detail', kwargs={'pk': self.object.id})


#
# SNIPPET
#
class SnippetContextMixin(CodeContextMixin):
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

class TagIndexView(generic.ListView, TagContextMixin):
    # Login mixin
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    context_object_name = 'tag_list'
    # template view
    template_name = 'tag/tag_list.html'

    def get_queryset(self):
        """

        :return: Codes only from the user
        """
        return Tag.objects.filter(owner=self.request.user)


class TagCreateView(generic.CreateView, TagContextMixin):
    model = Tag
    fields = ['title']
    success_url = reverse_lazy('codeapp:tag_list')
    template_name = 'tag/tag_form.html'

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

        return super(TagCreateView, self).form_valid(form)


class TagDetailView(generic.DetailView, TagContextMixin):
    model = Tag
    template_name = 'tag/tag_detail.html'


class TagUpdateView(generic.UpdateView, TagContextMixin):
    model = Tag
    fields = ['title']
    template_name = 'tag/tag_form_update.html'