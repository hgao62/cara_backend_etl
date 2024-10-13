"""main python file for project entry point"""
import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from .extract_data import (
    get_stock_history,
    get_stock_financials,
    get_exchange_rate,
    get_stock_currency_code,
    get_news,
)
from .load_data import save_df_to_db
logging.basicConfig(filename = 'projectLogs.log', filemode='a',
format='%(asctime)s - %(levelname)s - %(filename)s : %(lineno)s - %(message)s',
level=logging.INFO)
logger = logging.getLogger(__name__)


MYSQL_ENGINE = create_engine(r"mysql://root:Cara%40sheridan2023@localhost:3306/pythonkobe")
SQLITEENGINE = create_engine(
    r"sqlite:///C:\Users\zhang\OneDrive\Desktop\Udmy\Kobe_Python\mySqlite.db") 
ENGINE_DIC = {
    "mysql": MYSQL_ENGINE,
    "sqlite": SQLITEENGINE
}

def main(database_type : str) -> None:
    """
    main function to retrieve stcok information and history
    """
    engine = ENGINE_DIC[database_type]
    google_hist = get_stock_history("GOOG",period='1y')
    save_df_to_db(google_hist,"stock_history", engine = engine)
    google_major_holder = get_stock_financials("goog")
    ex_rate = get_exchange_rate("usd", "eur", "1d")
    google_currency_code = get_stock_currency_code("goog")
    google_news = get_news("goog")
    print(google_hist)
    print(google_major_holder)
    print(ex_rate)
    print(google_currency_code)
    print(google_news)

if __name__ == "__main__":
    DB_TYPE = "mysql"
    logger.info('Start running stock ETL pipeline to save data to database %s', DB_TYPE)
    try:
        main(DB_TYPE)
        logger.info("Finish stock ETL and uploading data successfully.")
    except (ValueError, KeyError, SQLAlchemyError) as e:
        logger.exception("Stock ETL encounterred error due to %s", str(e))
