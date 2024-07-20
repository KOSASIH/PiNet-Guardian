import pandas as pd
from sklearn.model_selection import train_test_split
from ai_model.model_architecture import create_model

def train_model():
    data = pd.read_csv("data/traffic_data.csv")
    X = data.drop("label", axis=1)
    y = data["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = create_model()
    model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
    model.save("models/anomaly_detection_model.h5")
