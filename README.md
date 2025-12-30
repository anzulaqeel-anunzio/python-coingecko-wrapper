# CoinGecko Crypto Wrapper (Python)

A simple Python wrapper for the CoinGecko Cryptocurrency API.

## Features

-   **Ping**: Check API status.
-   **Simple Price**: Get current price of coins vs currencies.
-   **Coin List**: Fetch list of supported coins.
-   **No API Key Required**: Works with the free tier (demo) API.

## Installation

1.  **Clone the repository**
2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Install Package (Optional)**
    ```bash
    pip install .
    ```

## Usage

```python
from coingecko_wrapper import CoinGeckoClient

client = CoinGeckoClient()

# Check server status
if client.ping():
    print("CoinGecko API is up!")

# Get Bitcoin price in USD
price = client.get_price(ids='bitcoin', vs_currencies='usd')
print(f"Bitcoin Price: ${price['bitcoin']['usd']}")

# Get list of coins (first 5)
coins = client.get_coin_list()
for coin in coins[:5]:
    print(f"{coin['name']} ({coin['symbol']})")
```

## Contact

Developed for Anunzio International by Anzul Aqeel.
Contact +971545822608 or +971585515742.

## License

MIT


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
