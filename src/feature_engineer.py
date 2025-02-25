from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class FeatureEngineer:

    def __init__(self, data, target_column):
        self.data = data
        self.target_column = target_column

    def create_features(self):
        x = self.data.drop(columns=[self.target_column])
        y = self.data[self.target_column]

        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        print("Feauture engineering completed.")

        return X_train, X_test, y_train, y_test