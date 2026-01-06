"""
ML model for passenger profile analysis and flight preference prediction.
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

class PassengerAnalyzer:
    """Machine learning model for passenger profile analysis."""
    
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self.encoders = {}
        
    def preprocess_passenger_data(self, df):
        """Preprocess passenger data: age, gender, travel frequency."""
        df_processed = df.copy()
        
        # Encode categorical features
        categorical_cols = ['gender', 'preferred_airline', 'travel_class']
        for col in categorical_cols:
            if col in df.columns:
                self.encoders[col] = LabelEncoder()
                df_processed[col] = self.encoders[col].fit_transform(df[col])
        
        # Feature engineering
        if 'age' in df.columns:
            df_processed['age_group'] = pd.cut(df['age'], 
                                             bins=[0, 18, 30, 50, 100], 
                                             labels=[0, 1, 2, 3])
        
        return df_processed
    
    def train(self, X, y):
        """Train ML model on passenger data."""
        X_processed = self.preprocess_passenger_data(X)
        self.model.fit(X_processed, y)
        
    def predict_preferences(self, passenger_data):
        """Predict flight preferences based on passenger profile."""
        processed_data = self.preprocess_passenger_data(passenger_data)
        return self.model.predict(processed_data)
    
    def save_model(self, path='models/passenger_model.pkl'):
        """Save trained model and encoders."""
        import os
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump({'model': self.model, 'encoders': self.encoders}, path)
        
    def load_model(self, path='models/passenger_model.pkl'):
        """Load trained model and encoders."""
        data = joblib.load(path)
        self.model = data['model']
        self.encoders = data['encoders']

if __name__ == "__main__":
    analyzer = PassengerAnalyzer()
    print("Passenger analyzer initialized successfully.")
