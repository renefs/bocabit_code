import logging
from django.contrib.auth.mixins import AccessMixin
from django.views import generic


logger = logging.getLogger('webapp.users')


class AccountProfileView(generic.TemplateView, AccessMixin):
    template_name = "profile.html"