import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess_regression_data(csv_path):
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=['Country', 'AQI Value'])
    features = ['CO AQI Value', 'Ozone AQI Value', 'NO2 AQI Value', 'PM2.5 AQI Value']
    X = df[features]
    y = df['AQI Value']
    return X, y