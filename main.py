"""main python file for project entry point"""
from extract_data import (
    get_stock_history,
    get_stock_financials,
    get_exchange_rate,
    get_stock_currency_code,
    get_news,
)


def main():
    google_hist = get_stock_history("goog")
    google_major_holder = get_stock_financials("goog")
    ex_rate = get_exchange_rate("usd", "eur", "1d")
    google_currency_code = get_stock_currency_code("goog")
    google_news = get_news("goog")


if __name__ == "__main__":
    main()
