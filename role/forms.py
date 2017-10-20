from django import forms


class PetOwnerForm(forms.ModelForm):
    class Meta:
        fields = ['pet_type', 'name', 'birthday']