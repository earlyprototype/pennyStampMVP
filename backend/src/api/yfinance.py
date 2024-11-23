import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            return None  # Return None if no data is found
        return data.to_dict('records') # Convert to a list of dictionaries
    except Exception as e:
        raise  # Re-raise the exception to be handled by the calling function