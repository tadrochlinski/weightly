from django import forms
from .models import WeightEntry

class WeightForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super(WeightForm, self).__init__(*args, **kwargs)
        self.user = user

    class Meta:
        model = WeightEntry
        fields = ['weight', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'min': 30, 'max': 200}),
        }

    def save(self, commit=True):
        weight_entry = super().save(commit=False)
        weight_entry.user = self.user
        weight_entry.bmi = self.calculate_bmi(self.user.userprofile)
        weight_entry.suggested_calories = self.calculate_calories(self.user.userprofile, weight_entry)
        if commit:
            weight_entry.save()
        return weight_entry

    def calculate_bmi(self, userprofile):
        height_in_meters = userprofile.height / 100
        bmi = self.cleaned_data['weight'] / (height_in_meters ** 2)
        rounded_bmi = round(bmi, 2)

        bmi_categories = [
            (18.5, "Underweight"),
            (24.9, "Normal weight"),
            (29.9, "Overweight"),
            (34.9, "First degree obesity"),
            (39.9, "Second degree obesity"),
            (float('inf'), "Third degree obesity"),
        ]

        bmi_category = next(category for upper_limit, category in bmi_categories if rounded_bmi < upper_limit)

        bmi_charfield = f'{rounded_bmi} | {bmi_category}'

        return bmi_charfield

    def calculate_calories(self, user_profile, weight_entry):
        bmr = 10 * weight_entry.weight + 6.25 * user_profile.height - 5 * user_profile.age

        if user_profile.gender == 'M':
            bmr += 5
        elif user_profile.gender == 'F':
            bmr -= 161

        return bmr