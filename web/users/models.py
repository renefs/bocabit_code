import uuid

from django.core.exceptions import ValidationError
from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """

    """
    avatar = models.URLField()
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)


class UserGroup(models.Model):
    """

    """
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name='owned_groups', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, blank=True)
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    class Meta:
        """"""
        unique_together = (("title", "owner"),)
        ordering = ('created_at', )
