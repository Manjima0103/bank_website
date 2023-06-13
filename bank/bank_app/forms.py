from django import forms

DISTRICT_CHOICES = [
    ('Kasaragod', 'Kasaragod'),
    ('Kannur', 'Kannur'),
    ('Kozhikode', 'Kozhikode'),
    ('Wayanad', 'Wayanad'),
    ('Malappuram', 'Malappuram'),
]

BRANCH_CHOICES = {
    'Kasaragod': ['Branch 1', 'Branch 2', 'Branch 3'],
    'Kannur': ['Branch 4', 'Branch 5', 'Branch 6'],
    'Kozhikode': ['Branch 7', 'Branch 8', 'Branch 9'],
    'Wayanad': ['Branch 10', 'Branch 11', 'Branch 12'],
    'Malappuram': ['Branch 13', 'Branch 14', 'Branch 15'],
}

ACCOUNT_TYPE_CHOICES = [
    ('Savings Account', 'Savings Account'),
    ('Current Account', 'Current Account'),
]

MATERIALS_PROVIDE_CHOICES = [
    ('Debit Card', 'Debit Card'),
    ('Credit Card', 'Credit Card'),
    ('Cheque Book', 'Cheque Book'),
]

class BankForm(forms.Form):
    name = forms.CharField(label='Name')
    dob = forms.DateField(label='DOB', widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'type': 'number'}))
    gender = forms.ChoiceField(label='Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    phone = forms.CharField(label='Phone Number')
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address', widget=forms.Textarea)
    district = forms.ChoiceField(label='District', choices=DISTRICT_CHOICES)
    branch = forms.ChoiceField(label='Branch', choices=[], required=False)
    account_type = forms.ChoiceField(label='Account Type', choices=ACCOUNT_TYPE_CHOICES)
    materials_provide = forms.MultipleChoiceField(label='Materials Provide', choices=MATERIALS_PROVIDE_CHOICES, widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].choices = [(choice, choice) for choice in BRANCH_CHOICES.get(self['district'].value()) or []]
