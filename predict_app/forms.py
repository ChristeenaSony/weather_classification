from django import forms
from .models import WeatherData

class WeatherForm(forms.ModelForm):
    class Meta:
        model = WeatherData
        fields = [
            'temperature',
            'humidity',
            'wind_speed',
            'precipitation',
            'cloud_cover',
            'atmospheric_pressure',
            'uv_index',
            'season',
            'visibility',
        ]
        widgets = {
            'cloud_cover': forms.Select(choices=[
                ('clear', 'clear'),
                ('cloudy', 'cloudy'),
                ('overcast', 'overcast'),
                ('partly cloudy', 'partly cloudy'),
            ]),
            'season': forms.Select(choices=[
                ('Autumn', 'Autumn'),
                ('Spring', 'Spring'),
                ('Summer', 'Summer'),
                ('Winter', 'Winter'),    
            ]),
        }
