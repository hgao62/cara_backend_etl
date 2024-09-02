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

def get_stock_financials(stock:str) -> pd.DataFrame:
    """_summary_

    Args:
        stock (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    stock_info = yf.Ticker(stock)
    return stock_info.major_holders

def get_exchange_rate(from_currency:str, to_currency:str, interval:str) -> pd.DataFrame:
    """_summary_

    Args:
        from_currency (str): _description_
        to_currency (str): _description_
        interval (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    ticker = f'{from_currency}{to_currency}=X'
    
    # Download the historical FX data
    fx_data = yf.download(ticker, interval=interval)
    
    return fx_data

def get_stock_currency_code(stock:str)-> pd.DataFrame:
    ticker=yf.Ticker(stock)
    currency_code=ticker.fast_info["currency"]
    return currency_code

def get_news(stock:str)->pd.DataFrame:
    stock_info = yf.Ticker(stock)
    
    news = stock_info.news
    
    news_df = pd.DataFrame(news)
    
    return news_df


