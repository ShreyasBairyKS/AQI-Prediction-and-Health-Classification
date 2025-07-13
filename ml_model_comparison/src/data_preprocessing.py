import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(subset=['Country', 'AQI Category'], inplace=True)
    label_encoder = LabelEncoder()
    df['AQI_Category_Encoded'] = label_encoder.fit_transform(df['AQI Category'])
    features = ['CO AQI Value', 'Ozone AQI Value', 'NO2 AQI Value', 'PM2.5 AQI Value']
    X = df[features]
    y = df['AQI_Category_Encoded']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, label_encoder
