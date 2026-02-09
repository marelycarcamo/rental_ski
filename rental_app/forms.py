from django import forms
from django.core.exceptions import ValidationError
from datetime import date

class ArrendarEquipoForm(forms.Form):
    # Campo de fecha con validación integrada y estilos personalizados
    fecha= forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'style': 'font-size: 1.5rem; background: gray; color: white;',  # Estilos del template
            'class': 'form-control'  # Clase Bootstrap opcional
        }),
        label="Selecciona la fecha de arrendamiento",
        help_text="Mínimo hoy en adelante"  # Texto de ayuda
    )

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < date.today():
            raise ValidationError("¡La fecha no puede ser anterior a hoy!")
        return