from src.data_loader import DataLoader
from src.data_cleaner import DataCleaner
from src.feature_engineer import FeatureEngineer
from src.model_evaluator import ModelEvaluator

def main():
   file_path = "data/your_dataset.csv" # path to your dataset
   target_column = "target_column" # name of the target column

   loader = DataLoader(file_path)
   data = loader.load_data()

   if data is not None:
        cleaner = DataCleaner(data)
        data = cleaner.handle_missing_values()
        data = cleaner.remove_outliers()

        engineer = FeatureEngineer(data, target_column)
        X_train, X_test, y_train, y_test = engineer.create_features()

        evaluator = ModelEvaluator(X_train, X_test, y_train, y_test)
        evaluator.train_and_evaluate()

   else:
         print("Data not loaded")


if __name__ == "__main__":
     main()
