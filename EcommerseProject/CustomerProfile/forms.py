from django import forms
from .models import Address, Country, State, City


addresstypechoice = [('Home', 'Home'), ('Work', 'Work')]
class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        exclude=['customer']

        labels = {
            'fname':'First Name',
            'lname':'Last Name',
            'mobile':'Mobile Number',
            'address_type':'Address Type'
        }
        widgets = {
            'fname':forms.TextInput(attrs={'placeholder':'Enter First Name'}),
            'lname':forms.TextInput(attrs={'placeholder':'Enter Last Name'}),
            'mobile':forms.TextInput(attrs={'placeholder':'Enter Mobile Number'}),
            'address':forms.Textarea(attrs={'placeholder':'Enter Address'}),
            # 'address_type':forms.RadioSelect(choices=addresstypechoice,attrs={'required':'True'})
        }


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['state'].queryset = State.objects.none()
    #     self.fields['city'].queryset = City.objects.none()
    #
    #     if 'country' in self.data:
    #         try:
    #             country_id = int(self.data.get('country'))
    #             self.fields['state'].queryset = State.objects.filter(country_id=country_id).order_by('state_name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['state'].queryset = self.instance.country.state_set.order_by('country_name')
    #
    #     if 'state' in self.data:
    #         try:
    #             state_id = int(self.data.get('state'))
    #             self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('city_name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['city'].queryset = self.instance.state.city_set.order_by('state_name')
    #
