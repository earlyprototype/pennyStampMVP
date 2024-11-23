from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=3600)  # 1-hour TTL


@cached(cache)
def get_cached_data(ticker, start_date, end_date):
    return cache.get((ticker, start_date, end_date))


def cache_data(ticker, start_date, end_date, data):
    try:
        cache[(ticker, start_date, end_date)] = data
    except Exception as e:
        raise RuntimeError(f"Failed to cache data: {str(e)}")
