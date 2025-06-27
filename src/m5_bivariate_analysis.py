import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class BivariateAnalysis():
    def __init__(self, df: pd.DataFrame, figure_size: tuple= (8, 4)):
        self.df = df
        self.figure_size = figure_size
        self.numerical_columns = df.selectdtypes(include="numbers")
        self.categorical_columns =  df.selectdtypes(include="exclude")

    def num_analysis(self):
        """
        Plots the relationships between two numerical features
        """
        pass
        
    def cat_analysis(self):
        """
        Plots the relationships between two categorical features
        """
        pass
        
    def num_cat_analysis(self, feat1, feat2):
        """
        Plots the relationships between a categorical and numerical feature
        """
        sns.boxplot(x=feat1, y=feat2, data=self.df, kde=True)
        plt.title(f"{feat1} vrs {feat2}")
        plt.xlabel(f"{feat1}")
        plt.ylabel(f"{feat2}")
        plt.xticks(rotation=45)
        plt.show()


