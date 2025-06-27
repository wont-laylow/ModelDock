import pandas as pd
from abc import abstractmethod, ABC
import logging
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class MissingValues(ABC):
    @abstractmethod
    def analyze(self):
        pass

    @abstractmethod
    def drop_null(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def handle_null(self, strategy: str = "mean", fill_constant=None) -> pd.DataFrame:
        pass


class HandleMissingValues(MissingValues):

    def __init__(self, df: pd.DataFrame, axis=0, thresh=None, figsize: tuple = (12, 8)):
        self.is_missing_values = False
        self.axis = axis
        self.thresh = thresh
        self.df = df
        self.figsize = figsize

    def analyze(self, cmap: str = "coolwarm" ):
        """
        Function to display null values on a heatmap
        """
        print("Generating heatmap")
        plt.figure(figsize= self.figsize)
        sns.heatmap(data=self.df.isnull(), cbar=True, cmap=cmap)
        plt.title("Missing Values Heatmap")
        plt.show() 

    def drop_null(self) -> pd.DataFrame:
        """
        Function to drop all null values in the dataset
        """
        logging.info(f"Dropping missing values with axis={self.axis} and thresh={self.thresh}")

        df_cleaned = self.df.dropna(axis=self.axis, thresh=self.thresh)

        logging.info("Missing values dropped.")
        return df_cleaned

    def handle_null(self, strategy: str= "mean", fill_constant=None)-> pd.DataFrame:
        """
        Function to display null values in the dataset
        """
        logging.info(f"Handling missing values using strategy: {strategy}")
        df = df.copy()

        for col in df.columns:
            if df[col].isnull().any():
                if df[col].dtype in [np.float64, np.int64, np.int32]:
                    if strategy == "mean":
                        fill_value = df[col].mean()
                    elif strategy == "median":
                        fill_value = df[col].median()
                    elif strategy == "zero":
                        fill_value = 0
                    elif strategy == "mode":
                        fill_value = df[col].mode()[0]
                    elif strategy == "constant":
                        fill_value = fill_constant if fill_constant is not None else "missing"
                    else:
                        raise ValueError(f"Unsupported strategy '{strategy}' for numerical column: {col}")
                
                    df[col].fillna(fill_value, inplace=True)
                    
        logging.info("Missing value handling complete.")
        return df





