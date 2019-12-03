"""lambdata - a collection of data science helper functions """

import pandas as pd 
import numpy as np 

# sample code 

ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))

# sample functions 

def increment(x):
    return (x + 1)


df = pd.DataFrame([1, 2, 3, 4, 5, 6, 7, 8, 9, np.NaN, 0, 0])

def check_nulls(df):
  result = df.isnull().sum().sum()
  return print('There are', result, 'null values in this dataframe')

# works for a single column 

def bag_tag(data, segments=10):
  edge = segments + 1
  labels = range(1, edge, 1) 
  return pd.qcut(data, q=segments, labels=labels)