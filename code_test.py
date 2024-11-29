import requests
from requests import Response
from typing_extensions import Any, Dict, List

#black "file path" will organize the file better
#mypy will check if the definition of the variables is well done(?)
#isort will sort imports in alphabetic order
#autodoc to add a description to a function


def get_crypto_prices(site) -> Any:
    """_summary_

    Args:
        site (str): _description_

    Returns:
        Any: _description_
    """
    url = site
    params: Dict[str, str] = {"ids": "bitcoin,ethereum,litecoin", "vs_currencies": "usd"}
    response: Response = requests.get(url, params=params, )
    prices: Any = response.json()
    return prices


crypto_prices = get_crypto_prices("https://api.coingecko.com/api/v3/simple/price")
for coin, value in crypto_prices.items():
    print(f"{coin.capitalize()}: ${value['usd']}")
REGISTRY: List[int] = [
    1213,
    21412431,
    5432543534,
    6436554645,
    23452532523,
    3252352,
    5644363,
    7657657567,
    1234242,
    8655686,
    2314324234,
    8757687,
    2345235,
    7969769,
    2343424,
    78687,
    798789,
]
