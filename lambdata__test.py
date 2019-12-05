#import the unit test package and functions we want to test out
import unittest
from lambdata_rileythejones import CleanData
from lambdata_rileythejones.df_utils import df_null, df_random, df_random_column  

class LambdataTests(unittest.TestCase):
    """Test for existence of the sample data"""
    def test_df_samples(self):
        self.assertIsNotNone(df_null)
        self.assertIsNotNone(df_random)

    """Test the function that checks for nulls against two different dataframes"""
    def test_check_nulls(self):
        dirty_data = CleanData(df_null)
        self.assertEqual(dirty_data.check_nulls(), 1)
        clean_data = CleanData(df_random)
        self.assertEqual(clean_data.check_nulls(), 0)
    
    """ Check that the shape of the filtered dataframe is different from the original"""
    def test_outlier_filter(self):
        df_filtered = CleanData(df_random).outlier_filter()
        self.assertNotEqual(df_filtered.shape, df_random.shape)

    """ Test that the number of unique values is the same as what's specified"""
    def test_bag_tag(self):
        df_category = CleanData(df_random).bag_tag(df_random_column, 100)
        self.assertEqual(len(df_category.unique()), 100)

if __name__ == '__main__':
    unittest.main()