import uuid

from django.db import models

from users.models import CustomUser


class UsageTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    factor = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Usage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="usages",
    )
    usage_type = models.ForeignKey(
        UsageTypes,
        on_delete=models.CASCADE,
        related_name="usages",
    )
    usage_at = models.DateTimeField()
    amount = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
