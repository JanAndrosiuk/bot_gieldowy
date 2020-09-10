import websocket, json
import sqlite3
import time, datetime

conn = sqlite3.connect('BTC.db')
cur = conn.cursor()

def on_message(ws, message):
    response = json.loads(message)
    kursbtc = response['data'][0]['p']

#    unix = time.time()
#    date = datetime.datetime.now()
    timestamp = int(response['data'][0]['t'])
    dt = datetime.datetime.fromtimestamp(int(timestamp) / 1000)
    date = dt.strftime("%Y-%m-%d %H:%M:%S")
    cur.execute('''CREATE TABLE IF NOT EXISTS Kursy(
                    id INTEGER PRIMARY KEY, 
                    kurs INTEGER, 
                    czas TEXT
                )''')

    cur.execute('''INSERT INTO Kursy(kurs, czas) VALUES(?, ?)''', (kursbtc, date))
    #cur.execute('''DELETE FROM Kursy WHERE rowid NOT IN (SELECT rowid FROM Kursy ORDER BY rowid LIMIT 100)''')
    conn.commit()
    print(kursbtc)
    time.sleep(1)

    # file_path = 'test.txt'
    # with open(file_path, "a") as test:
    #    test.write(str(kursbtc) + "\n")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    #ws.send('{"type":"subscribe","symbol":"AAPL"}')
    #ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    #ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=bs252a7rh5rc90r524v0",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    print(type(ws))
    ws.run_forever()





