from django.db.models import manager
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404


class BaseManager(manager.Manager):
    def get_queryset(self):
        return QuerySet(self.model, using=self._db).exclude(is_deleted=True)