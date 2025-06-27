import pandas as pd
from m1_ingest_data import Ingestor
import os

class GetSummary():
    def __init__(self, df) -> pd.DataFrame:
        self.df = df

    def get_summary(self):
        print("Running basic validation...")
        print("Shape:", self.df.shape)
        print("Duplicates:", self.df.duplicated().sum())
        print("Missing values:\n", self.df.isnull().sum())
        print("Data types:\n", self.df.dtypes)
        print("Statistical summary:", self.df.describe(include='all'))


# if __name__ == "__main__":
#     current_dir = os.path.dirname(__file__)
#     file_path = os.path.join(current_dir, "..", "test_data", "archive.zip")
#     file_path = os.path.abspath(file_path)

#     summary = GetSummary()
#     summary.get_summary()


    