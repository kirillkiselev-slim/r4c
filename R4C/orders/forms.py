from django import forms
from customers.models import Customer
from robots.models import Robot

class UserOrderForm(forms.Form):
    model = forms.CharField()
    version = forms.CharField()
    email = forms.EmailField()

    def clean_model(self):
        model = self.cleaned_data.get("model").upper()
        models = [robot.model for robot in Robot.objects.all()]
        if model not in models:
            raise forms.ValidationError("Not a valid model")
        return model

    def clean_version(self):
        version = self.cleaned_data.get("version").upper()
        versions = [robot.version for robot in Robot.objects.all()]
        if version not in versions:
            raise forms.ValidationError("Not a valid version")
        return version.upper()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        search_email = Customer.objects.filter(email=email)
        if not search_email.exists():
            raise forms.ValidationError("User does not exist")
        return email