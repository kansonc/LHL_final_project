# Package Imports
import pandas as pd
import numpy as np



# Column Cleaning Function assignments
def preprocessing_initial_transformations_func(pp_df_strip_str, pp_df_new_dtype, pp_df_new_col_name):
    '''
    Applies replacement functions to all values of the dataframe to 
    1. convert all whitespace-only and null values to None, NaN, and NaT as needed,
    2. convert all columns to a desired dtype, and
    3. rename columns 
    
    Args:
        initial_df: original data at ingestion
        pp_df_changes: takes the preprocessing_df_merged
    
    Global Variables:
        delivery_df_pp: contains all changes to the dataset from this function
        pp_df_report_of_changes: shows all columns and which functions were applied
        pp_df_post_stats: shows if the changes have been implemented
        
    '''
    from modules.mod_0_preliminary import delivery_df_raw, delivery_df
    ### Create a Dataframe/Series of the original columns from data ingestion
    df_initial_col_names = pd.DataFrame(delivery_df_raw.columns, columns= ['old_column_name'])

    ### Create a Report of Changes
    global pp_df_report_of_changes
    pp_df_report_of_changes = pd.concat(
        [df.set_index('old_column_name') for df in [
        df_initial_col_names
        ,pp_df_strip_str
        ,pp_df_new_dtype
        ,pp_df_new_col_name
        ]
        ]
        ,axis=1
        ,join='outer'
    ).reset_index()
    
    ### Create a 
    global delivery_df_pp
    delivery_df_pp = delivery_df_raw.copy()
    
    
    # Assign Functions as detailed
    for index, row in pp_df_report_of_changes.iterrows():
        for column, value in row.items():
            
            # Null values means no transformation needed
            if pd.notnull(value):
                
                # Temporarily store the column name to be transformed
                col_to_trans = pp_df_report_of_changes.at[index, 'old_column_name']
                
                # Clause to strip values
                if column == "strip_characters":
                    delivery_df_pp[col_to_trans] = pp_func_strip_chars(delivery_df_pp[col_to_trans], value)
                    
                # Clause to change data type
                if column == 'new_data_type':
                    delivery_df_pp[col_to_trans] = pp_func_dtype_change(delivery_df_pp[col_to_trans], value)
                
                # Clause to change the name
                if column == 'new_column_name':
                    delivery_df_pp = pp_func_change_col_name(delivery_df_pp, col_to_trans, value)
    
    
    # Create a table that shows the changes
    global pp_df_post_stats                
    pp_df_post_stats = pp_post_stats(delivery_df_raw, delivery_df_pp)
    



def pp_func_strip_chars(column_series: pd.Series, string_to_strip: str):
    '''
    Transforms and returns a series by removing a user defined string
    '''
    column_series.replace(string_to_strip, '', inplace=True, regex=True)
    return column_series


def pp_func_dtype_change(column_series: pd.Series, data_type_to_change_to: str):
    '''
    Transforms and returns a series (Arg: column_series) by changing its data type (Arg: data_type_to_change_to)
    
    '''
    # The following conditional
    if data_type_to_change_to == "float" or data_type_to_change_to == "integer":
        column_series = column_series.replace(r'^\s*$'  , np.NaN, regex=True)
        column_series = column_series.replace(['NaN', 'None', ''], np.NaN)
        
        if data_type_to_change_to == "integer":
            column_series = pd.to_numeric(column_series, downcast=data_type_to_change_to,errors="coerce")
            column_series = column_series.astype('Int64')
            return column_series
        
        else:
            column_series = pd.to_numeric(column_series, downcast=data_type_to_change_to,errors="coerce")
            return column_series
    

    elif data_type_to_change_to == "date" or data_type_to_change_to == "time":
        column_series.replace(r'^\s*$'  , pd.NaT, inplace=True, regex=True)
        column_series.replace('NaN'     , pd.NaT, inplace=True)
        column_series.replace('None'    , pd.NaT, inplace=True)
        column_series.replace(''        , pd.NaT, inplace=True)
       
        if data_type_to_change_to == "date":
            column_series = pd.to_datetime(column_series, yearfirst=True, format='mixed')
            return column_series
        else:
            column_series = pd.to_datetime(column_series, format='%H:%M:%S')
            return column_series
        
    else:    
        column_series.replace(r'^\s*$'  , '', inplace=True, regex=True)
        column_series.replace('NaN'     , '', inplace=True)
        column_series.replace('None'    , '', inplace=True)
        column_series = column_series.str.strip()
        
        if data_type_to_change_to == "string":
            column_series = column_series.astype(data_type_to_change_to)

            return column_series
        
        else:
            column_series = column_series.astype(data_type_to_change_to)
            return column_series
        
        
def pp_func_change_col_name(df: pd.DataFrame, old_column_name: str, new_column_name: str):
    '''
    Transforms a returns a dataframe by changing the name of a specified column
    '''
    df.rename(columns={old_column_name: new_column_name}, inplace=True)
    return df


def pp_post_stats(raw_data: pd.DataFrame, transformed_data: pd.DataFrame):
    '''
    Returns a DataFrame containing information of columns pre and post transformations 
    Only useful after preprocessing functions have been used.
    '''
    # Store the columns names as a list
    df_org_cols_list = raw_data.columns.tolist()

    # Stage an empty dataframe
    df_pp_post_stats = pd.DataFrame(columns=['column'
                                                ,'data_type_before'
                                                ,'data_type_after'
                                                ,'null_count_before'
                                                ,'null_count_after'
                                                ]
    )

    # Create stats for before and after quick clean of the data
    for column_name in df_org_cols_list:
        row_data =  pd.DataFrame(
                    {'column'           :[column_name]
                    ,'data_type_before' :[raw_data[column_name].dtype]
                    ,'data_type_after'  :[transformed_data[column_name].dtype]
                    ,'null_count_before':[raw_data[column_name].isna().sum()]
                    ,'null_count_after' :[transformed_data[column_name].isna().sum()]
                    }
        )
        df_pp_post_stats = pd.concat([df_pp_post_stats, row_data], ignore_index=True)
    
    return df_pp_post_stats