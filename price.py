import requests
import pandas as pd

def fetch_klines(symbol, interval="1m", limit=1440):
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    
    df = pd.DataFrame(data, columns=[
        "Open Time", "Open", "High", "Low", "Close", "Volume",
        "Close Time", "Quote Asset Volume", "Number of Trades",
        "Taker Buy Base Asset Volume", "Taker Buy Quote Asset Volume", "Ignore"
    ])
    df["Open Time"] = pd.to_datetime(df["Open Time"], unit="ms")
    df["Close Time"] = pd.to_datetime(df["Close Time"], unit="ms")
    df = df[["Open Time", "Open", "High", "Low", "Close", "Volume"]]
    return df

btc = fetch_klines("BTCUSDT")
eth = fetch_klines("ETHUSDT")

btc.to_csv("btc_24h_1m.csv", index=False)
eth.to_csv("eth_24h_1m.csv", index=False)

print("Saved as btc_24h_1m.csv and eth_24h_1m.csv")
