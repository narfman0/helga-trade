import requests
from helga import settings
from helga.plugins import command, random_ack


CRYPTO_URL = 'https://min-api.cryptocompare.com/data/price?fsym={from}&tsyms={to}'
CRYPTO_LIST = 'https://www.cryptocompare.com/api/data/coinlist/'
TARGET_CURRENCY = getattr(settings, 'TRADE_TARGET_CURRENCY', 'USD')
crypto_data = None


def logic(args):
    crypto_data = fetch_crypto_data()
    if len(args) == 1:
        symbol = args[0].lower()
        try:
            price = try_crypto(symbol)
            return symbol + ' is currently trading at ' + str(price) + ' ' + TARGET_CURRENCY
        except ValueError:
            return 'Symbol ' + symbol + ' not supported!'
    return 'Try asking for help? Unknown command: ' + ', '.join(args)


def try_crypto(symbol='btc'):
    """ Test out of symbol is crypto, and if so return price. Throw ValueError otherwise. """
    if symbol not in crypto_data:
        for crypto_symbol, data in crypto_data.items():
            if data['CoinName'] == symbol:
                symbol = crypto_symbol
    if symbol in crypto_data:
        response = requests.get(CRYPTO_URL).json()
        price = response[TARGET_CURRENCY]
        return int(price)
    raise ValueError(symbol + ' not available as crypto')


def fetch_crypto_data():
    """ Fetch and parse crypto data """
    global crypto_data
    if not crypto_data:
        response = requests.get(CRYPTO_LIST).json()
        crypto_data = {symbol.lower(): data for symbol, data in response['Data'].items()}
    return crypto_data


@command('trade', help='Stock, crypto, forex trade information plugin for helga\n!trade btc')
def trade(client, channel, nick, message, cmd, args):
    return logic(args)
