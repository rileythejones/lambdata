""""
utility functions for working with DataFrames

"""

import pandas as pd 
import numpy as np 

df_null = pd.DataFrame([1, 2, 3, 4, 5, 6, 7, 8, 9, np.NaN, 0, 0])

df_random = pd.DataFrame(np.random.randn(100, 3))

df_random_column = df_random[0]