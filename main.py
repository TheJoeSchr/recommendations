import ccxt
from pyfzf.pyfzf import FzfPrompt
fzf = FzfPrompt()


def main():
    exchange_list = ccxt.exchanges
    selected_exchange = []
    while not selected_exchange:
        selected_exchange = fzf.prompt(exchange_list)
        print(f"Selected exchange: {selected_exchange}")
    # Initialize the Binance exchange object
    exchange_name = selected_exchange[0]
    exchange = getattr(ccxt, exchange_name)()

    print('Asset selection')
    try:
        # Fetch the list of assets traded on Binance
        markets = exchange.load_markets()

        # Extract the asset symbols from the market data
        asset_symbols = list(markets.keys())

        # Filter only unique asset symbols
        unique_quote_symbols = set()
        for symbol in asset_symbols:
            # print(symbol)
            base, quote = symbol.split('/')
            unique_quote_symbols.add(quote)

        # Convert the set to a sorted list
        quote_list = sorted(list(unique_quote_symbols))

        selected_quote = []
        while not selected_quote:
            selected_quote = fzf.prompt(quote_list)
            print(f"Selected quote: {selected_quote}")

        unique_asset_symbols = set()
        for symbol in asset_symbols:
            # print(symbol)
            base, quote = symbol.split('/')
            if quote == selected_quote[0]:
                unique_asset_symbols.add(base)
                unique_asset_symbols.add(quote)

        asset_list = sorted(list(unique_asset_symbols))
        print(f"Assets traded on {selected_exchange[0]}:{len(asset_list)}")

        selected_asset = []
        while not selected_asset:
            selected_asset = fzf.prompt(asset_list)
            print(f"Selected asset: {selected_asset}/{selected_quote[0]}")

        # Print the list of assets
        # print("Assets traded on Binance:")
        # for asset in asset_list:
        #     print(asset)
        # print(f"Assets traded on Binance:{len(asset_list)}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
