from ..src.api.yfinance import fetch_stock_data

data = fetch_stock_data("AAPL", "2024-01-01", "2024-01-05")
print(data)