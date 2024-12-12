import talib

def calculate_sma(data, column='Close', period=20):

    return talib.SMA(data[column], timeperiod=period)

def calculate_ema(data, column='Close', period=20):

    return talib.EMA(data[column], timeperiod=period)

def calculate_rsi(data, column='Close', period=14):

    return talib.RSI(data[column], timeperiod=period)

def calculate_macd(data, column='Close'):

    macd, signal, hist = talib.MACD(data[column], fastperiod=12, slowperiod=26, signalperiod=9)
    return macd, signal, hist
