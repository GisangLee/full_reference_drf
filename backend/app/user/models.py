from django.db import models

from app.common.models import BaseModel


class User(BaseModel):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = verbose_name
        ordering = ["-created"]
