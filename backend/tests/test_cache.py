from ..src.utils.cache import get_cached_data, cache_data
from ..src.api.yfinance import fetch_stock_data

ticker = "MSFT"
start_date = "2024-01-01"
end_date = "2024-01-05"

# Clear the cache
cache_data(ticker, start_date, end_date, None)

# Fetch and cache data
test_data = fetch_stock_data(ticker, start_date, end_date)
cache_data(ticker, start_date, end_date, test_data)

# Retrieve from cache
retrieved_data = get_cached_data(ticker, start_date, end_date)

# Assert that the cached data matches the fetched data
assert test_data == retrieved_data

print(retrieved_data)