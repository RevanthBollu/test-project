from django.forms import ModelForm

from testapp.models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
