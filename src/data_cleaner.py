import pandas as pd

class DataCleaner:

    def __init__(self, data):
        self.data = data

    # handling missing values  
    def handle_missing_values(self):
        self.data.fillna(self.data.mean(), inplace=True)
        print("Missing Values handled")
        return self.data
    
    # removing outliers using the z score method
    def remove_outliers(self, threshold=3):
        z_scores = (self.data - self.data.mean()) / self.data.std()
        self.data = self.data[(z_scores.abs() < threshold).all(axis=1)]
        print("Outliers removed")
        return self.data