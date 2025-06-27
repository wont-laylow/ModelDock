import pandas as pd
import seaborn as sns


class CheckOutliers():

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.numerical_columns = df.selectdtypes(include="numbers")
        self.categorical_columns =  df.selectdtypes(include="exclude")
        self.outlier_feats = []

    def iqr_method(self):
        for col in self.numerical_df.columns:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)]
            print(f'{col}: {len(outliers)} outliers')

    def zscore_method(self):
        pass

    def chisq_method(self):
        pass
    

    def _visualize_outliers(self):
        """
        To visualize outliers found in any of the above functions used.
        """
        for col in self.outlier_feats:
            sns.boxplot(self.df[col])
            

class HandleNumericalOutliers(CheckOutliers):
    def __init__(self, df: pd.DataFrame):
        super().__init__()

    def something():
        pass


class HandleCategoricalOutliers(CheckOutliers):
    def __init__(self, df: pd.DataFrame):
        super().__init__()

    def something():
        pass




