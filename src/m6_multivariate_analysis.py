import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


class MultivariateAnalysis():
    def __init__(self, df: pd.DataFrame, figure_size: tuple= (12, 10)):
        self.df = df
        self.figure_size = figure_size

    def corr_heatmap(self, df):
        """
        Generate a scatter plot
        """
        plt.figure(figsize=self.figure_size)
        sns.heatmap(data=df.corr(), annot=True, cmap="cool")
        plt.title("Correletion Heatmap")
        plt.show()
        
    def pair_plot(self, df):
        """
        Generate a pair plot
        """
        sns.pairplot(df)
        plt.suptitle("Pair plot of selected Features", y=1.02)
        plt.show()