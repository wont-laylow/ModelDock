import zipfile
import pandas as pd
import tempfile
import os
from abc import ABC, abstractmethod


class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Abstract Method to ingest any form of data uploaded"""
        pass

class Ingestor(DataIngestor):
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp()
        self.supported_formats = ['.csv', '.xlsx', '.xls', '.parquet']

    def _unzip_files(self, file_path):
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(self.temp_dir)

            return self.temp_dir


    def _load_df(self, file_path: str) -> pd.DataFrame:
        extension = os.path.splitext(file_path)[1].lower()
        if extension == ".csv":
            return pd.read_csv(file_path)
        elif extension in [".xlsx", ".xls"]:
            return pd.read_excel(file_path)
        elif extension == ".parquet":
            return pd.read_parquet(file_path)
        else:
            raise ValueError(f"Unsupported file type: {extension}")


    def ingest(self, file_path: str) -> pd.DataFrame:
        if file_path.lower().endswith("zip"):
            extracted_path = self._unzip_files(file_path)

            for root, _, files in os.walk(extracted_path):
                for file in files:
                    if os.path.splitext(file)[1].lower() in self.supported_formats:
                        return self._load_df(os.path.join(root, file))
                    else:
                        raise FileNotFoundError("No supported data file found in the zip archive.")
                    
        else: 
            return self._load_df(file_path)
                    

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "..", "test_data", "archive.zip")
    file_path = os.path.abspath(file_path)


    ingestor = Ingestor()
    df = ingestor.ingest(file_path)
    print(df.head()) 

    