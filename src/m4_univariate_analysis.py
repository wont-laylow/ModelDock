import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


class UnivariateAnalysis():
    def __init__(self, df: pd.DataFrame, figure_size: tuple= (8, 4)):
        self.df = df
        self.figure_size = figure_size
        self.numerical_columns = df.selectdtypes(include="numbers")
        self.categorical_columns =  df.selectdtypes(include="exclude")

    def num_analysis(self, figure_size, fig_type : str = "hist", spec_feat: str = None):
        """
        Function to conduct univariate analysis on numerical spec_feats. Creates histograms and boxplots.
        """ 
        spec_feat = spec_feat.lower()
        plt.figure(figsize=figure_size)
        if spec_feat in self.numerical_columns:
            if spec_feat is not None:
                if fig_type.lower() == "hist":
                    print("Generating Histogram")
                    sns.histplot(data=self.df[spec_feat], kde=True)

                if fig_type.lower() == "boxplt":
                    print("Generating Boxplot")
                    sns.boxplot(data=self.df[spec_feat], kde=True)

                plt.title(f"Distribution of {spec_feat}")
                plt.xlabel(f"{spec_feat}")
                plt.ylabel("Count")
                plt.xticks(rotation=45)
                plt.show()

        else: 
            for col in self.df.columns:
                if col in self.numerical_columns:

                    # hist
                    print("Generating Histogram")
                    sns.histplot(data=self.df[col], kde=True)
                    plt.title(f"Distribution of {spec_feat}")
                    
                    # boxplot
                    print("Generating Boxplot")
                    sns.boxplot(self.df[col], kde=True, bins=30)
                    plt.title(f"Distribution of {col}")

                plt.xlabel(f"{self.df[col]}")
                plt.ylabel("Count")
                plt.xticks(rotation=45)
                plt.show()

    def cat_analysis(self, figure_size, spec_feat: str = None):
        """
        Function to conduct univariate analysis on categorical spec_feats. Creates countplots.
        """ 
        spec_feat = spec_feat.lower()
        plt.figure(figsize=figure_size)
        if spec_feat is not None and spec_feat in self.categorical_columns:
            sns.countplot(x=spec_feat, data=self.df[self.categorical_columns])
            plt.title(f"Value counts of {spec_feat}")
            plt.xlabel(spec_feat)
            plt.ylabel("Frequency")
            plt.tight_layout()
            plt.show()

        else:
            for col in self.df.columns:
                if col in self.categorical_columns:
                    sns.countplot(x=self.df[col], data=self.df[self.categorical_columns])
                plt.title(f"Value counts of {self.df[col]}")
                plt.xlabel(self.df[col])
                plt.ylabel("Frequency")
                plt.tight_layout()
                plt.show()
                
    

