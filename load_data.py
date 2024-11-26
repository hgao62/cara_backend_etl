"""Calculate daily return and accumulative daily return, load data into Sqlite database"""
import logging
import pandas as pd
#import sqlalchemy library(used for interact with db using pandas)
from sqlalchemy import create_engine
import sqlalchemy

ENGINE = create_engine(
    r"sqlite:///C:\Users\zhang\OneDrive\Desktop\Udmy\Kobe_Python\mySqlite.db") 

logger = logging.getLogger(__name__)
def save_df_to_db(
    data_frame : pd.DataFrame,
    table_name : str,
    engine : sqlalchemy.engine.base.Engine = ENGINE,
    if_exists : str="append",
    dtype : dict=None,
) -> None:
    """
    Function to send a DataFrame to an SQL database.
    
    Args:
        df (pd.DataFrame): DataFrame to be sent to the SQL database.
        table_name (str): Name of the table in the SQL database.
        engine: Database engine type, in this case, it could be sqlite or mysql.
        if_exists (str): Action to take if the table already exists in the SQL database.
                         Options: "fail", "replace", "append" (default: "append").
        dtype (dict, optional): Dictionary of column names and data types to be used 
                                when creating the table.
        
    Returns:
        None. This function logs a message to confirm that data has been sent to the SQL database.
    """
    logger.info("Load data into a SQL database")
    data_frame.to_sql(
        name = table_name,
        con = engine,
        if_exists = if_exists,
        index = False,
        dtype = dtype
    )
    print('data saved successfully.')
    logging.info("DataFrame saved successfully to table %s in the SQL database.", table_name)
