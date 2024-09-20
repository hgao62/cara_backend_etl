"""Calculate daily return and accumulative daily return, load data into Sqlite database"""
import logging
from pandas import DataFrame
#2. import sqlalchemy library(used for interact with db using pandas)
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import sqlalchemy

ENGINE = create_engine(
    r"sqlite:///C:\Users\zhang\OneDrive\Desktop\Udmy\Kobe_Python\mySqlite.db") 

def save_df_to_db(
    df : DataFrame,
    table_name : str,
    engine : sqlalchemy.engine.base.Engine,
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
    try:
        df.to_sql(
            name = table_name,
            con = engine,
            if_exists = if_exists,
            index = False,
            dtype = dtype
        )

        logging.info("DataFrame saved successfully to table %s in the SQL database.", table_name)
    except SQLAlchemyError as e:
        # Catch any SQLAlchemy-specific database errors
        logging.error("Database error saving DataFrame to table %s: %s", table_name, str(e))
    except df.errors.EmptyDataError as e:
        # Catch pandas-specific errors (e.g., if the DataFrame is empty)
        logging.error("Empty data error in DataFrame: %s", str(e))
    except ValueError as e:
        # Catch ValueError (for example, if there's an invalid column data type)
        logging.error("Value error in saving DataFrame: %s", str(e))
  