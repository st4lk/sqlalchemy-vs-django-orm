from django.db import models


class FkRight(models.Model):
    pass


class FkLeft(models.Model):
    right = models.ForeignKey(FkRight, on_delete=models.CASCADE)
