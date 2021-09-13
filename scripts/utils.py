import os
import pandas as pd

def read_xlsx(path:str, sheet_name:str)->pd.core.frame.DataFrame:
    """
    Reads and returns the excel file as dataframe from the 
    provided path.
    
    Args:
        path:str -> Path of the dataframe
        sheet_name:str -> Sheet name in the excel
    """
    try:
        return pd.read_excel(path, sheet_name = sheet_name)
    except Exception as error:
        raise Exception('Caught this error: ' + repr(error))

def extract_date_features(df:pd.core.frame.DataFrame,
                          date_column:str='datetime',
                          feature_name:str='hour')->list:
    """
    Extract date features(i.e. hour, month, week, dayofweek) and returns
    as a list to store as a new column. 
    
    Args:
        df:pd.core.frame.DataFrame
        date_column_name:str
        feature_name:str -> (i.e. hour, month, week, dayofweek)
    
    """
    try:
        df[date_column] = pd.to_datetime(df[date_column])

        if feature_name=='hour':
            return df[date_column].dt.hour
        elif feature_name=='dayofweek':
            return df[date_column].dt.dayofweek
        elif feature_name=='year':
            return df[date_column].dt.year
        elif feature_name=='month':
            return df[date_column].dt.month
        elif feature_name=='week':
            return df[date_column].dt.isocalendar().week.astype("int64")
        else:
            raise NotImplementedError
            
    except Exception as error:
        raise Exception('Caught this error: ' + repr(error))
    
def get_commision(provider:str, order_count:int)->float:
    """
    This function calculates and returns monthly commision
    given provider and order count for each month.
    
    Args:
        provider:str
        order_count:str
    """
    
    if provider=='tom_jerry':
        return 8000
    
    elif provider=='roadrunner':
        return order_count*50
    
    elif provider=='donald_duck':
        return order_count*50
    
    elif provider=='micky_mouse':
        
        above_500_orders = order_count-500
        above_500_orders = above_500_orders if above_500_orders >0 else 0
        return 10000+(above_500_orders*10)
    
def group_by_and_sum_rows(data:pd.core.frame.DataFrame, 
                            group_by_columns:list, 
                            column_to_sum:str='order_date',
                            resulted_column_name:str='total_orders')->pd.core.frame.DataFrame:
    """
    Grouped by the given column list and calculated summation the provided column and store result 
    as a new column.
    
    Args:
        data:pd.core.frame.DataFrame
        group_by_columns:list
        column_to_sum:str
        resulted_column_name:str
    
    Returns: 
        Updated dataframe-> consists of grouped columns and calculated result as a new column.
    
    """    
    df_grouped = data[group_by_columns+[column_to_sum]].groupby(group_by_columns).sum().reset_index()
    df_grouped = df_grouped.rename(columns={column_to_sum: resulted_column_name})
    return df_grouped


def resolve_converted_wide_table_index_issue(df:pd.core.frame.DataFrame)->pd.core.frame.DataFrame:
    '''
    This function resolves the issue created because of using pandas pivot function. Resets the
    dataframe index and returns updated dataframe.
    
    '''
    
    #setting index column name to none for getting rid of multiple index column name by pivot function
    df.index.name = None
    #reset index
    df = df.reset_index()
    return df