"""Enum definition for constant variables in extract_data.py"""
from enum import Enum

class SelectedColumns(Enum):
    """This class should define Enums for column names of the data 
       frame output of the get_stock_financials function in extract_data.py

    Args:
        Enum (_type_): Enum 
    """
    INDEX = "index"  # The date column
    TAX_EFFECT_UNUSUAL_ITEMS = "Tax Effect of Unusual Items"
    TAX_RATE_CALCS = "Tax Rate For Calcs"
    NORMALIZED_EBIT = "Normalized EBIT"
    TOTAL_UNUSUAL_ITEMS = "Total Unusual Items"
    NET_INCOME_FROM_CONTINUING_OPS = "Net Income From Continuing Ops"
    RECONCILED_DEPRECIATION = "Reconciled Depreciation"
    RECONCILED_COST_REVENUE = "Reconciled Cost Of Revenue"
    EBITDA = "EBITDA"
    EBIT = "EBIT"
    NET_INTEREST_INCOME = "Net Interest Income"
    INTEREST_EXPENSE = "Interest Expense"
    INTEREST_INCOME = "Interest Income"
    NORMALIZED_INCOME = "Normalized Income"
    NET_INCOME_FROM_CONTINUING_OPERATIONS = "Net Income From Continuing Operations"
    TOTAL_EXPENSE = "Total Expenses"
    TOTAL_OPERATING_EXPENSES = "Total Operating Expenses"


class ExchangeOutputColumns(Enum):
    """This class should define Enums for column names of the data 
       frame output of the get_exchange_rate function in extract_data.py


    Args:
        Enum (_type_): Enum
    """
    DATE = "Date"
    TICKER = "Ticker"
    FROM_CURRENCY = "From Currency"
    TO_CURRENCY = "To Currency"
    OPEN = "Open"
    HIGH = "High"
    LOW = "Low"
    CLOSE = "Close"
    ADJ_CLOSE = "Adj Close"


class NewsOutputColumns(Enum):
    """This class should define Enums for column names of the data 
       frame output of the get_news function in extract_data.py

    Args:
        Enum (_type_): Enum
    """
    STOCK = "stock"
    UUID = "uuid"
    TITLE = "title"
    PUBLISHER = "publisher"
    LINK = "link"
    PROVIDER_PUBLISH_TIME = "provider_publish_time"
    TYPE = "type"
