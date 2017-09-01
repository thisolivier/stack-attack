from django import forms
from models import User, Student, Instructor

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password',)
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder':'Email'}),
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        # By passing email_skip, we can choose whether or not to check for unique emails
        self.exclude_unique_email = kwargs.pop('skip_email', False)
        self.confirm_password = kwargs.pop('c_pass', (False, False))
        super(UserForm, self).__init__(*args, **kwargs)

        if self.confirm_password[0]:
            self.fields['c_password'] = forms.CharField(
                widget=forms.PasswordInput,
                label="Confirm Password",
                required=self.confirm_password[1]
                )

    def validate_unique(self):
        exclude = self._get_validation_exclusions()
        if self.exclude_unique_email:
            # Disable validations of uniqueness here
            exclude.append('email')
        self.instance.validate_unique(exclude=exclude)

class RegisterInstructorForm(forms.ModelForm):
    code = forms.CharField(label="Top Secret Code")
    class Meta:
        model = Instructor
        fields = ('name',)

class RegisterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name')
