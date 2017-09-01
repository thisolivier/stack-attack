from django import forms
from models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('email', 'password',)

    def validate_unique(self):
        # Disable validations of uniqueness here
        pass