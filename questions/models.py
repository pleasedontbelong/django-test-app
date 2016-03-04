from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    title = models.CharField('Question Title', max_length=150, blank=True)

    def __unicode__(self):
        return self.title
