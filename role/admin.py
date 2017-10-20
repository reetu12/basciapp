# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from basicapp.admin import owners_admin
from django.contrib import admin as django_admin
from .models import Pets
from .forms import PetOwnerForm


class PetAdmin(django_admin.ModelAdmin):
    list_display = ['name', 'pet_type', 'birthday', 'owner']
    list_filters = ['pet_type']
    search_fields = ['name']

admin.site.register(Pets)

class PetOwnerAdmin(PetAdmin):
    list_display = ['name', 'pet_type', 'birthday']
    form = PetOwnerForm

    def get_queryset(self, request):
        # restrict pets to only owner's ones
        return super().get_queryset(request).filter(owner=request.user)

    # set necessary permissions by default
    def has_module_permission(self, *args, **kwargs):
        return True

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True

    def save_model(self, request, obj, *args, **kwargs):
        obj.owner = request.user  # set owner automatically
        super().save_model(request, obj, *args, **kwargs)

owners_admin.register(Pets, PetOwnerAdmin)