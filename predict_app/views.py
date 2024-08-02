from django.shortcuts import render
import pandas as pd
import pickle
from .forms import WeatherForm


with open('data.pkl', 'rb') as file:
    data = pickle.load(file)
    rf = data['model']
    scaler = data['scaler']
    label_encoders = data['label_encoders']
    target_encoder = data['target_encoder']


def preprocess_data(df, label_encoders, scaler):
    for feature, le in label_encoders.items():
        df[feature] = df[feature].apply(lambda x: x if x in le.classes_ else 'Unknown')
        df[feature] = le.transform(df[feature])
    
    numerical_features = ['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)', 'Atmospheric Pressure', 'UV Index', 'Visibility (km)']
    df[numerical_features] = scaler.transform(df[numerical_features])
    return df

def home(request):
    form = WeatherForm()
    return render(request,'home.html',{'form':form})

def predict_weather(request):
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            input_data = {
                'Temperature': [data['temperature']],
                'Humidity': [data['humidity']],
                'Wind Speed': [data['wind_speed']],
                'Precipitation (%)': [data['precipitation']],
                'Cloud Cover': [data['cloud_cover']],
                'Atmospheric Pressure': [data['atmospheric_pressure']],
                'UV Index': [data['uv_index']],
                'Season': [data['season']],
                'Visibility (km)': [data['visibility']],
            }
            input_df = pd.DataFrame(input_data)
            preprocessed_input = preprocess_data(input_df, label_encoders, scaler)
            prediction = rf.predict(preprocessed_input)
            predicted_label = target_encoder.inverse_transform(prediction)[0]
            return render(request,'result.html',{'prediction':predicted_label})

    else:
        form = WeatherForm()

    return render(request,'home.html',{'form':form})



