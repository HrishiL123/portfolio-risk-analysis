import yfinance as yf
import pandas as pd

def fetch_price_data(tickers, start, end):
    """
    Fetch adjusted close prices for single or multiple tickers.
    Always returns a DataFrame with tickers as columns and dates as index.

    tickers: str or list of str
    start, end: date strings "YYYY-MM-DD"
    """
    # Download data
    data = yf.download(tickers, start=start, end=end, progress=False)

    # Case 1: MultiIndex columns (multiple tickers)
    if isinstance(data.columns, pd.MultiIndex):
        # Try to extract 'Adj Close' first
        if 'Adj Close' in data.columns.get_level_values(0):
            adj_close = data.xs('Adj Close', axis=1, level=0)
        else:
            # Fallback to 'Close'
            adj_close = data.xs('Close', axis=1, level=0)

    # Case 2: Single ticker returns DataFrame with 'Adj Close'
    elif 'Adj Close' in data.columns:
        adj_close = data['Adj Close'].to_frame(name=tickers if isinstance(tickers, str) else tickers[0])
    elif 'Close' in data.columns:
        adj_close = data['Close'].to_frame(name=tickers if isinstance(tickers, str) else tickers[0])
    # Case 3: Single ticker returns Series
    elif isinstance(data, pd.Series):
        adj_close = data.to_frame(name=tickers if isinstance(tickers, str) else tickers[0])
    else:
        raise ValueError("No 'Adj Close' or 'Close' data found. Check tickers/date range.")

    # Ensure index is datetime
    adj_close.index = pd.to_datetime(adj_close.index)

    return adj_close
