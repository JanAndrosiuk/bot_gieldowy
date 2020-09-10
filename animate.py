import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
import numpy as np
import time

conn = sqlite3.connect('BTC.db')
cur = conn.cursor()
count = 0
id_wiersza = 0
fig, ax = plt.subplots(1, 1, figsize=(6,4))
act_czas = []
act_kurs = []
while True:
    if count == 0 and id_wiersza == 0:
        cur.execute('''SELECT * FROM Kursy''')
        dane = cur.fetchall()
#       tutaj trzeba zaznaczyć id wiersza, żeby później wiedzieć co doszło
        id_wiersza = len(dane)
        print("z pętli if: ", id_wiersza)
        count = count + 1
        df = pd.DataFrame(dane)
        ticks = df[0].tolist()
        dane_kurs = df[1].tolist()
        dane_czas = df[2].tolist()
        ax.plot(dane_czas, dane_kurs)
        ax.aspect = 'auto'
        plt.pause(0.0001)
        print("T")
        plt.show()
        plt.draw()
        print("TE")
        act_czas = np.append(act_czas, dane_czas)
        act_kurs = np.append(act_kurs, dane_kurs)


    else:
        time.sleep(1)
        plt.pause(0.0001)
        cur.execute('''SELECT * FROM Kursy WHERE rowid > ''' + str(id_wiersza))
        dane = cur.fetchall() #nowe dane
        df = pd.DataFrame(dane)
        df_c = df[2].tolist()
        df_k = df[1].tolist()
        id_wiersza = id_wiersza + len(dane) #zaktualizowanie id_wiersza o nowe dane
        acc = np.append(act_czas, df_c)
        ack = np.append(act_kurs, df_k)
        ax.plot(acc, ack)
        ax.aspect = 'auto'
        print("T", acc, ack)
        #plt.show()
        plt.draw()
        print("TE")
        act_czas = acc
        act_kurs = ack
        print("z pętli else: ", id_wiersza)










#dane = pd.read_sql_query('''SELECT * FROM Kursy''', conn)
#xdane = dane[-100:]
#print(xdane)
#        ax.tick_params(axis='x', labelsize=8)
#ax = plt.gca()
#plt.plot(xdane['czas'], xdane['kurs'])
#plt.xticks(rotation='vertical')
#ax.tick_params(axis='x', labelsize=8)
#plt.tight_layout()
#plt.show()