import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
import numpy

conn = sqlite3.connect('BTC.db')
cur = conn.cursor()
count = 0
id_wiersza = 0
hl, = plt.plot([], [])
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
        hl.set_xdata(numpy.append(hl.get_xdata(), ticks))
        hl.set_ydata(numpy.append(hl.get_ydata(), dane_kurs))
        plt.xticks(ticks, dane_czas, rotation='vertical')
        plt.tight_layout()
        plt.show()
        plt.draw()

    else:
        cur.execute('''SELECT * FROM Kursy WHERE rowid > ''' + str(id_wiersza))
        dane = cur.fetchall() #nowe dane
        id_wiersza = id_wiersza + len(dane) #zaktualizowanie id_wiersza o nowe dane

        print("z pętli else: ", id_wiersza)
        continue









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