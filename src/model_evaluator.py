from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class ModelEvaluator:
    def __init__(self, X_train, X_test, y_train, y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.model = RandomForestClassifier()


    def train_and_evaluate(self):
        self.model.fit(self.X_train, self.y_train)
        predictions = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, predictions)
        print(f"Model Accuracy: {accuracy:.2f}")
        return accuracy