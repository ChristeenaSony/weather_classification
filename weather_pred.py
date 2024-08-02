import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier


w_data = pd.read_csv(r'F:\archive\weather_classification_data.csv')


x = w_data.drop(['Weather Type', 'Location'], axis=1)
y = w_data['Weather Type']





from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)


label_encoders = {}
categorical_features = ['Cloud Cover', 'Season']
for feature in categorical_features:
    le = LabelEncoder()
    x_train[feature] = le.fit_transform(x_train[feature])
    x_test[feature] = le.transform(x_test[feature])
    label_encoders[feature] = le

target_encoder = LabelEncoder()
y_train = target_encoder.fit_transform(y_train)


scaler = StandardScaler()
numerical_features = ['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)', 'Atmospheric Pressure', 'UV Index', 'Visibility (km)']
x_train[numerical_features] = scaler.fit_transform(x_train[numerical_features])
x_test[numerical_features] = scaler.transform(x_test[numerical_features])


rf = RandomForestClassifier(random_state=42)
rf.fit(x_train, y_train)


with open('data.pkl', 'wb') as file:
    pickle.dump({
        'model': rf,
        'scaler': scaler,
        'label_encoders': label_encoders,
        'target_encoder': target_encoder
    }, file)


