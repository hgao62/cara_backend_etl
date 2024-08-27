import yfinance as yf
import pandas as pd

def get_stock_history(stock:str)->pd.DataFrame:
    """_summary_

    Args:
        stock (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    stock_info = yf.Ticker(stock)
    hist = stock_info.history(period='1mo')
    return hist