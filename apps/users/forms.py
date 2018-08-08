import account.forms
from django import forms
from django.conf import settings
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _
from .models import ApplicationForm

from account.hooks import hookset
from account.forms import SignupForm
from django.forms import ModelForm
from apps.employee.models import *
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget


class UserForm(ModelForm):
    #user_signature = JSignatureField()
    user_signature = JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#333'}))
    class Meta:
        model = ApplicationForm
        fields = '__all__'
        widgets = {
            'convicted_or_not': forms.RadioSelect,
            'allowed_in_usa':forms.RadioSelect,
            'work_eligible_usa':forms.RadioSelect,
            'domicile_address':forms.RadioSelect,
            'law_suite':forms.RadioSelect,
            'compensation_claim':forms.RadioSelect,
            'other_city':forms.RadioSelect,
            'Martial_status':forms.Select(attrs={'class':'form-control', 'required':'required'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'required': 'required'})

        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = False
