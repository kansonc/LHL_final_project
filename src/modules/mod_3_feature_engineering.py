# Package Imports
import pandas as pd
import numpy as np

# Column Cleaning Function assignments
def feature_engineering_intial_transformations_func(processed_df: pd.DataFrame, fe_df_changes: pd.DataFrame):
    '''
    Takes columns from the preprocessed dataframe and assigns feature engineering functions
    functions to transform the data.  Does not drop the columns
    deemed "excluded" from the model.  
    
    Args:
        initial_df: original data at ingestion
        pp_df_changes: takes the preprocessing_df_merged
    
    
    Returns:
        dataframe of pp changes
    '''
   
    # Assign Functions as detailed
    for index, row in fe_df_changes.iterrows():
        for column, value in row.items():
            
            # Null values means no transformation needed
            if pd.notnull(value):
                
                # Temporarily store the column name to be transformed
                col_to_trans = fe_df_changes.at[index, 'column_name']
                

                # Clause to one-hot encode
                if column == 'encoding_prefix':
                    clean_df = fe_func_one_hot_encoding(clean_df, col_to_trans, value)
                    
                # Clause to create ordinal hierarchies
                if column == 'ordinal_hierarchy':
                    clean_df[f"{col_to_trans}_ordinal"] = fe_func_ordinal_hierarchy(clean_df[col_to_trans], value)
    
    return clean_df

def fe_func_one_hot_encoding(df: pd.DataFrame, column_name: str, prefix_value: str):
    '''
    Args:
        Takes the dataframe containing all completed transformations, 
        the series from the original dataframe at column you wish to encode
        and the prefix the encoding will append to return "prefix_value"
    
    Returns:
        Entire Dataframe containing all completed tranformations with the one-hot encoded columns appended
    '''
    df = pd.concat( [df
                    ,pd.get_dummies( df[column_name]
                                    ,prefix=prefix_value).astype('Int64')]
                    , axis=1)
    return df


def fe_func_ordinal_hierarchy(column_series: pd.Series, ordinal_hierarch_dic: dict):
    '''
    Transforms and returns a series by changing its values from strings to interger based on a specified ordinal hierarchy.
    Would be best practice to name the series that this function returns with "_ordinal" appened
    '''
    column_series.replace(ordinal_hierarch_dic, regex=True, inplace=True)
    column_series = column_series.astype('Int64')
    return column_series