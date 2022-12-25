from django import forms

from .models import Member


class UserEdit(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'user',
            'avatar',
            'online',
        ]
