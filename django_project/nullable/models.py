from django.db import models


# docs: https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.Field.nulls
class NullableFieldsModel(models.Model):
    value = models.CharField(max_length=50)
