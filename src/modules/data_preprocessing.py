# Package Imports
import pandas as pd
import numpy as np

# Data Ingestation
delivery_df = pd.read_csv(r'../data/delivery_2_excel_edits.csv')

# Column Cleaning Functions

def keep_number(column, data_type):
    '''
    args:    
        column = pandas dataframe column or series
        data_type = numeric data type 
    returns:
        numeric data
    '''
    column = column.str.replace(r'\D', '').astype(data_type)
    return column


## Strip (min) from time taken and convert to Integer

