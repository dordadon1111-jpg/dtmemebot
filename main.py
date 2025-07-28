
import time
from live_fetcher import fetch_and_filter_tokens

while True:
    fetch_and_filter_tokens()
    time.sleep(10)
