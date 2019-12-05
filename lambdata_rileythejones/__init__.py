"""lambdata_rileythejones - a collection of data science helper functions """

import pandas as pd 
import numpy as np 
from scipy import stats

class CleanData:
    """
    functions to clean a dataset
    """
    def __init__(self, df):
        self.df = df
    """
    returns the total number of null values in the entire dataframe
    """
    def check_nulls(self):
      result = self.df.isnull().sum().sum()
      return result 
      # return print('There are', result, 'null values in this dataframe')

    """
    removes rows that have at least one value that is n-standard deviations from a column mean
    """

    def outlier_filter(self, deviations=2):
      return self.df[(np.abs(stats.zscore(self.df)) < deviations).all(axis=1)]

    """
    takes an array of data as an input and outputs integer labels the correspond to 
    proportional bin rank 
    """

    def bag_tag(self, data, segments=10):
      edge = segments + 1
      labels = range(1, edge, 1) 
      return pd.qcut(data, q=segments, labels=labels)

