"""Extract data from yahoo finance"""

import yfinance as yf
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None) 
pd.set_option('display.width', None)
def get_stock_history(stock: str) -> pd.DataFrame:
    """_summary_

    Args:
        stock (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    stock_info = yf.Ticker(stock)
    hist = stock_info.history(period="1mo")

    return hist


def get_stock_financials(stock: str)->pd.DataFrame:
    """_summary_

    Args:
        stock (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    ticker = yf.Ticker(stock)
    stock_financials = ticker.financials.transpose().reset_index()
    selected_columns = [
        'index',  # The date column
        'Tax Effect of Unusual Items',
        'Tax Rate For Calcs',
        'Normalized EBIT',
        'Total Unusual Items',
        'Net Income From Continuing Ops',
        'Reconciled Depreciation',
        'Reconciled Cost Of Revenue',
        'EBITDA',
        'EBIT',
        'Net Interest Income',
        'Interest Expense',
        'Interest Income',
        'Normalized Income',
        'Net Income From Continuing Operations',
        'Total Expenses',
        'Total Operating Expenses'
    ]
    
    # Select only the specific columns from the DataFrame
    stock_financials_selected = pd.DataFrame()
    for col in selected_columns:
        if col in stock_financials.columns:
            stock_financials_selected[col]= stock_financials[col]
        else:
            stock_financials_selected[col]= np.nan
    stock_financials_selected.rename(columns={'index':'date'},inplace=True)
    return stock_financials_selected

def get_exchange_rate(
    from_currency: str, to_currency: str, interval: str
) -> pd.DataFrame:
    """_summary_

    Args:
        from_currency (str): _description_
        to_currency (str): _description_
        interval (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    ticker = f"{from_currency}{to_currency}=X"

    # Download the historical FX data
    fx_data = yf.download(ticker, interval=interval)

    return fx_data


def get_stock_currency_code(stock: str) -> pd.DataFrame:
    ticker = yf.Ticker(stock)
    currency_code = ticker.fast_info["currency"]
    return currency_code


def get_news(stock: str) -> pd.DataFrame:
    stock_info = yf.Ticker(stock)

    news = stock_info.news

    news_df = pd.DataFrame(news)

    return news_df
