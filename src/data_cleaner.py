import pandas as pd
import numpy as np

class DataCleaner:

    def __init__(self, data):
        self.data = data

    # handling missing values with type-specific handling
    def handle_missing_values(self):
        # Handle numeric columns with mean
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            self.data[numeric_cols] = self.data[numeric_cols].fillna(self.data[numeric_cols].mean())
        
        # Handle categorical columns with mode
        cat_cols = self.data.select_dtypes(include=['object', 'category']).columns
        if len(cat_cols) > 0:
            for col in cat_cols:
                self.data[col] = self.data[col].fillna(self.data[col].mode()[0] if not self.data[col].mode().empty else "Unknown")
        
        print("Missing Values handled")
        return self.data
    
    # removing outliers using the z score method
    def remove_outliers(self, threshold=3):
        # Only apply to numeric columns
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) > 0:
            # Calculate z-scores only for numeric columns
            z_scores = (self.data[numeric_cols] - self.data[numeric_cols].mean()) / self.data[numeric_cols].std()
            # Create a mask of rows to keep
            mask = (z_scores.abs() < threshold).all(axis=1)
            # Apply the mask to the entire dataframe
            self.data = self.data[mask]
            print(f"Outliers removed ({self.data.shape[0]} rows remaining)")
        else:
            print("No numeric columns found for outlier detection")
            
        return self.data