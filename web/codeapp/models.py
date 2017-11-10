from django.db import models

# Create your models here.
from codeproject import settings
from users.models import User


class Tag(models.Model):
    title = models.CharField(max_length=50, blank=False)
    owner = models.ForeignKey(User, related_name='owned_tags')

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = (("title", "owner"),)
        ordering = ('title', )


class Workspace(models.Model):
    owner = models.ForeignKey(User, related_name='owned_workspaces')
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = (("title", "owner"),)
        ordering = ('title', )


class Code(models.Model):
    owner = models.ForeignKey(User, related_name='owned_codes')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='codes')
    workspaces = models.ManyToManyField(Workspace, blank=True, related_name='codes')
    is_private = models.BooleanField(default=True)

    class Meta:
        unique_together = (("title", "owner"),)
        ordering = ('created_at',)


class BaseSnippet(models.Model):
    language = models.CharField(max_length=100, choices=settings.LANGUAGE_CHOICES)
    version_number = models.IntegerField(default=1)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('created_at', )


class Snippet(BaseSnippet):
    author = models.ForeignKey(User, related_name='owned_snippets')
    code = models.ForeignKey(Code, related_name='snippets')
    title = models.CharField(max_length=200)


class Version(BaseSnippet):
    author = models.ForeignKey(User, related_name='owned_versions')
    snippet = models.ForeignKey(Snippet, related_name='versions')

    class Meta:
        unique_together = (("snippet", "version_number"),)
