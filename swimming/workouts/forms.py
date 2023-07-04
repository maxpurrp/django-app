from .models import Registrations
from django.forms import ModelForm, TextInput, NumberInput, Textarea

class RegistrationsForm(ModelForm):
    class Meta:
        model = Registrations
        fields = ['name', 'age', 'phone', 'purpose', 'comment']

        widgets = {
            'name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Ваше Имя'}),

            'age' : NumberInput(attrs={'min': '18', 'max': '65', 
                                       'class' : 'form-control',
                                       'placeholder' : 'Ваш возраст'}),

            'phone' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Номер в формате 89965592812'}),

            'purpose' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Ожидаемый результат'
            }),
            'comment' : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Комментарий'
            })
        }