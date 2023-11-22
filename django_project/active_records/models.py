from django.db import models


class M1(models.Model):

    value = models.CharField(max_length=50)
