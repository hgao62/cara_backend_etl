from enum import Enum


class Financial(Enum):
    """Enum for storing company's financial """
    TAX_RATE_FOR_CALCS = "Tax Rate For Calcs",
    NORMALIZED_EBIT =     "Normalized EBIT new",
    TOTAL_UNUSUAL_ITEMS =   "Total Unusual Items"
    
    
class StockPrice(Enum):
    TICKER = "stock name"
    CLOSE_PRICE = "close price"