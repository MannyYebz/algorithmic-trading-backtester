import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start, end):
    """
    Fetch historical stock price data from Yahoo Finance.

    Parameters:
        ticker : Stock symbol e.g. "AAPL", "SPY", "MSFT"
        start  : Start date e.g. "2020-01-01"
        end    : End date e.g. "2024-01-01"

    Returns:
        DataFrame with columns: Open, High, Low, Close, Volume
    """
    data = yf.download(ticker, start=start, end=end, auto_adjust=True)
    data.dropna(inplace=True)
    return data