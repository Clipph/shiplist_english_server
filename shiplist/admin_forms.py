from django import forms
from .models import Ship
from django.core.exceptions import ValidationError
from unidecode import unidecode
import re

class ShipAdminForm(forms.ModelForm):
    class Meta:
        model = Ship
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        # Original input
        half = cleaned_data.get('half', '')
        half_other = cleaned_data.get('half_other', '')

        # Normalize and clean text
        def normalize_text(text):
            text = unidecode(text)  # Transliterates foreign characters to ASCII
            text = re.sub(r'[^a-z0-9]', '', text.lower())
            return text

        half_norm = normalize_text(half)
        half_other_norm = normalize_text(half_other)

        # List of known forbidden base terms (will be normalized too)
        forbidden_values = [
            'knayle', 'knayl', 'knale', 'knayel', 'knaylee', 'kneyle',
            'knaylie', 'knaille', 'kn4yle', 'kn@yle', 'knay1e', 'knayie',
            'knayleish', 'knayleeish', 'knayleish', 'nayle', 'naylee',
            'naylie', 'nayleish', 'nayleeish', 'nayleish', 'nayleee',
            'knay', 'kale', 'shipper',
        ]
        forbidden_normalized = [normalize_text(val) for val in forbidden_values]

        has_error = False

        if half_norm in forbidden_normalized:
            self.add_error('half', f'"{half}" is not allowed.')
            has_error = True

        if half_other_norm in forbidden_normalized:
            self.add_error('half_other', f'"{half_other}" is not allowed.')
            has_error = True

        if has_error:
            raise ValidationError("Knayle cannot be shipped!")

        return cleaned_data
