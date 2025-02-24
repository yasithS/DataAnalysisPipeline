import pandas as pd

# load the data from csv
class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path

        def load_data(self):
            try:
                data = pd.read_csv(self.file_path)
                print("Data loaded successfully")
                return data
            except Exception as e:
                print(f"Error loding data: {e}")

