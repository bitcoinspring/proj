from django import forms

class OrderForm(forms.Form):
    values = (
        ('5', '$5'),
        ('10', '$10'),
        ('25', '$25'),
    )
    amount = forms.ChoiceField(choices=values)
    email = forms.EmailField()
    username = forms.CharField()

