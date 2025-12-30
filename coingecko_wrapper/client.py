# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import requests

class CoinGeckoClient:
    BASE_URL = "https://api.coingecko.com/api/v3"

    def __init__(self):
        """Initialize the CoinGecko client."""
        pass

    def _make_request(self, endpoint: str, params: dict = None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def ping(self) -> bool:
        """Check if API server is up."""
        data = self._make_request("ping")
        return "(V3) To the Moon!" in data.get("gecko_says", "")

    def get_price(self, ids: str, vs_currencies: str):
        """
        Get the current price of any cryptocurrencies in any other supported currencies that you need.
        example: client.get_price(ids='bitcoin', vs_currencies='usd')
        """
        return self._make_request("simple/price", params={
            "ids": ids,
            "vs_currencies": vs_currencies
        })

    def get_coin_list(self):
        """List all supported coins id, name and symbol."""
        return self._make_request("coins/list")

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
