import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

class TimeSeriesAnalysis:
    def __init__(self):
        self.model = None

    def fit(self, data):
        self.model = ARIMA(data, order=(5,1,0))
        self.model_fit = self.model.fit()

    def forecast(self, steps):
        forecast = self.model_fit.forecast(steps=steps)
        return forecast

    def visualize_forecast(self, data, forecast):
        print("Visualizing forecast...")
        plt.plot(data)
        plt.plot(forecast)
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.show()
