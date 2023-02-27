import uuid

from django.db import models


class BaseModel(models.Model):
    """
    Base model that adds a uuid field as the main ID field
    Also adds a created timestamp field.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class ProductModel(BaseModel):
    """
    Model storing data about products
    """

    name = models.CharField(max_length=1024, blank=False, null=False)
    description = models.TextField()
    product_number = models.CharField(max_length=1024, blank=False, null=False)
