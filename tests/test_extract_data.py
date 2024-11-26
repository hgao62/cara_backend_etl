"""Unit test extract_data.py"""
import pandas as pd
import yfinance as yf
from pytest_mock import MockerFixture
from ..extract_data import get_stock_history

def test_get_stock_history(mocker: MockerFixture) -> None:
    """This function should carry out unit test on get_stick_history function
    from extract_data.py

    Args:
        mocker (MockerFixture): an instance of MockerFixture
    """
    #Use mocker of pytest to patch or replace the Ticker class of the yf module.
    #When autospec=True is used, the mock will have the same interface as the real onject
    mock_ticker = mocker.patch.object(yf,'Ticker', autospec=True)
    sample_data = pd.DataFrame({
        "Date": pd.date_range(start = '2023-01-01', periods=30, freq='D'),
        "Open":[100+i for i in range(30)],
        "High":[110+i for i in range(30)],
        "Low":[50 + i for i in range(30)],
        "Close":[105 +i for i in range(30)],
        "Volume":[1000+i for i in range(30)],
        "Dividends":[0]*30,
        "Stock Splits": [0] *30,
        "Stock": ['GOOG']*30
    }).set_index('Date')

    mock_ticker.return_value.history.return_value = sample_data
    stock = 'GOOG'
    period = '1mo'
    result = get_stock_history(stock,period)

    assert isinstance(result, pd.DataFrame), "The result should be DataFrame"
    assert "Open" in result.columns, "Expected 'Open' column in the result"
    assert "High" in result.columns, "Expected 'High' column in the result"
    assert "Low" in result.columns, "Expected 'Low' column in the result"
    assert "Close" in result.columns, "Expected 'Close' column in the result"
    assert "Volume" in result.columns, "Expected 'Volume' column in the result"
    assert "Dividends" in result.columns, "Expected 'Dividends' column in the result"
    assert "Stock" in result.columns, "Expected 'Stock' column in the result"
    pd.testing.assert_frame_equal(result, sample_data, check_dtype = False)
    pd.testing.assert_index_equal(result.index,sample_data.index,
    "Expected result index match sample_data index")
