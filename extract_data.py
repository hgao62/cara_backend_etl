"""Extract data from yahoo finance"""

import yfinance as yf
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None) 
pd.set_option('display.width', None)
def get_stock_history(stock: str) -> pd.DataFrame:
    """this function should full stock history given a stock input 
        with period of 1 month

    Args:
        stock (str): stock ticker symbol

    Returns:
        pd.DataFrame: 1-month stock price history with columns of 
        date, open, high, low, close, volumn, dividens, stock
    """
    stock_info = yf.Ticker(stock)
    hist = stock_info.history(period="1mo")

    return hist


def get_stock_financials(stock: str)->pd.DataFrame:
    """this function should get fiancial metrics given a stock input

    Args:
        stock (str): stock ticker symbol

    Returns:
        pd.DataFrame: stock financials of a stock including 
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
    """this function should download the foreign exchange rate
    given input of swap currencies and interval

    Args:
        from_currency (str): currency to convert from
        to_currency (str): currency to covnert to
        interval (str): time interval by which exchange rate is retrieved

    Returns:
        pd.DataFrame: foreign exhange rates between two currencies by specified time interval
        information including date, Ticker Name, from currency, to currency, open, high, low,
        close, adjusted close 
    """
    ticker = f"{from_currency}{to_currency}=X"

    # Download the historical FX data
    fx_data = yf.download(ticker, interval=interval)
    fx_data.drop('Volume',axis=1, inplace=True)
    fx_data.insert(0,'Ticker',ticker)
    fx_data.insert(1,'From Currency',from_currency)
    fx_data.insert(2,'To Currency',to_currency)
    return fx_data


def get_stock_currency_code(stock: str) -> pd.DataFrame:
    """this function should retrieve currency this stock belongs to

    Args:
        stock (str): stock ticker symbol

    Returns:
        pd.DataFrame: trading currency code of the stock
    """
    ticker = yf.Ticker(stock)
    currency_code = ticker.fast_info["currency"]
    return currency_code


def get_news(stock: str) -> pd.DataFrame:
    """this function should return the news of a given stock

    Args:
        stock (str): stock ticker symbol

    Returns:
        pd.DataFrame: news of a given stock 
    """
    stock_info = yf.Ticker(stock)

    news = stock_info.news

    news_df = pd.DataFrame(news)

    return news_df
