# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Bridge(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512)