from django.db import models


class BaseModelMixin:
    created = models.DateTimeField(verbose_name="생성일시", auto_now_add=True, db_index=True)
    updated = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    class Meta:
        abstract = True


class BaseModel(models.Model):
    created = models.DateTimeField(verbose_name="생성일시", auto_now_add=True, db_index=True)
    updated = models.DateTimeField(verbose_name="수정일시", auto_now=True)

    class Meta:
        abstract = True
