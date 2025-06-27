import pandas as pd
import os


class GetSummary():

    def __init__(self, df) -> pd.DataFrame:
        self.df = df

    def get_summary(self):
        summary_report = {
            "Shape": self.df.shape,
            "Duplicate Rows": self.df.duplicated().sum(),
            "Missing Values": self.df.isnull().sum().to_frame(name="Missing Count"),
            "Data Types": self.df.dtypes.to_frame(name="Data Type"),
            "Statistical Summary": self.df.describe(include='all').transpose()
        }
        return summary_report


# if __name__ == "__main__":
#     current_dir = os.path.dirname(__file__)
#     file_path = os.path.join(current_dir, "..", "test_data", "archive.zip")
#     file_path = os.path.abspath(file_path)

#     summary = GetSummary()
#     print(summary.get_summary())


    