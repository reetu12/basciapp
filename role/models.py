# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Pets(models.Model):
    pet_type = models.CharField('animal type', max_length=8, choices=[
        ('cat', 'Cat'),
        ('dog', 'Dog'),
    ])
    name = models.CharField('name', max_length=32)
    birthday = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet_type
