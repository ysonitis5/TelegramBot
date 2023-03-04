import telebot
import ccxt

BOT_TOKEN='secret'

exchange = ccxt.bitmex()
markets = exchange.load_markets()

for symbol in markets:
    print(symbol)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['ETH'])
def btc_data(message):
    # Create an instance of the CCXT BitMEX exchange object
    exchange = ccxt.bitmex()

    # Get the daily OHLCV (open, high, low, close, volume) data for Bitcoin
    data = exchange.fetch_ohlcv('ETH/USDT:USDT', '1d')

    # Get the daily open, close, volume, and open interest
    daily_open = data[-1][1]
    daily_close = data[-1][4]
    daily_volume = exchange.fetch_ticker('ETH/USDT:USDT')['quoteVolume']
    daily_open_interest = data[-1][5]  # The open interest value is at index 5 in the OHLCV array

    # Format the data as a string
    response = f'Daily Open: {daily_open:.2f}\n' \
               f'Daily Close: {daily_close:.2f}\n' \
               f'Daily Volume: {daily_volume:.2f}\n' \
               f'Daily Open Interest: {daily_open_interest:.2f}'

    # Reply to the user with the data
    bot.reply_to(message, response)


@bot.message_handler(commands=['BTC'])
def btc_data(message):
    # Create an instance of the CCXT BitMEX exchange object
    exchange = ccxt.bitmex()

    # Get the daily OHLCV (open, high, low, close, volume) data for Bitcoin
    data = exchange.fetch_ohlcv('BTC/USDT:USDT', '1d')

    # Get the daily open, close, volume, and open interest
    daily_open = data[-1][1]
    daily_close = data[-1][4]
    daily_volume = exchange.fetch_ticker('BTC/USDT:USDT')['quoteVolume']
    daily_open_interest = data[-1][5]  # The open interest value is at index 5 in the OHLCV array

    # Format the data as a string
    response = f'Daily Open: {daily_open:.2f}\n' \
               f'Daily Close: {daily_close:.2f}\n' \
               f'Daily Volume: {daily_volume:.2f}\n' \
               f'Daily Open Interest: {daily_open_interest:.2f}'

    # Reply to the user with the data
    bot.reply_to(message, response)

@bot.message_handler(commands=['LINK'])
def btc_data(message):
    # Create an instance of the CCXT BitMEX exchange object
    exchange = ccxt.bitmex()

    # Get the daily OHLCV (open, high, low, close, volume) data for Bitcoin
    data = exchange.fetch_ohlcv('LINK/USD:BTC', '1d')

    # Get the daily open, close, volume, and open interest
    daily_open = data[-1][1]
    daily_close = data[-1][4]
    daily_volume = exchange.fetch_ticker('LINK/USD:BTC')['quoteVolume']
    daily_open_interest = data[-1][5]  # The open interest value is at index 5 in the OHLCV array

    # Format the data as a string
    response = f'Daily Open: {daily_open:.2f}\n' \
               f'Daily Close: {daily_close:.2f}\n' \
               f'Daily Volume: {daily_volume:.2f}\n' \
               f'Daily Open Interest: {daily_open_interest:.2f}'

    # Reply to the user with the data
    bot.reply_to(message, response)

@bot.message_handler(commands=['HELP'])
def btc_data(message):


    # Format the data as a string
    response = '/BTC for Bitcoin daily info \n' \
               '/ETH for Ethereum daily info \n' \
               '/LINK for Chainlink daily info \n' \
               '/HELP for commands '

    # Reply to the user with the data
    bot.reply_to(message, response)

@bot.message_handler(commands=['HELP'])
def btc_data(message):


    # Format the data as a string
    response = '/BTC for Bitcoin daily info \n' \
               '/ETH for Ethereum daily info \n' \
               '/LINK for Chainlink daily info \n' \
               '/HELP for commands '

    # Reply to the user with the data
    bot.reply_to(message, response)


# Start the bot
bot.polling()
