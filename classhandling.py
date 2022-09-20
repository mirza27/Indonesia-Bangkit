import pandas as pd
import datetime as d

class Handling():
    def __init__(self, *addreses):
        for address in addreses:
            self.dt = pd.read_csv(address) # membaca data

            # membuat nama outname file
            self.outname = list(address)
            self.outname = "".join(self.outname[-8:])

            # membuat tahun untuk datetime
            self.year = int("".join(self.outname[-8:-4]))

            # mengahpus kolom yang tidak perlu
            del self.dt['Tahunan']
            del self.dt['Wilayah Kereta Api']
            del self.dt['_id']

            self.dt = self.dt.iloc[2] # mengambil data dari wilayah jawa
            self.dt = pd.DataFrame(self.dt)

            self.dt[''] = [i for i in range(1,13)] # membuat kolom baru untuk dijadikan format index
            self.dt = self.dt.set_index('')

            # membuat kolom 'bulan' sebagai pertama, dan mengganti menjadi format bulan dan tahun
            self.dt.insert(0, 'bulan', [i for i in range(1,13)])
            self.dt['bulan'] = [d.datetime(self.year,i, 1).strftime('%Y-%m') for i in self.dt['bulan']]


            self.dt.columns =['bulan', 'jumlah'] # merename semua kolom


            #self.dt.to_csv(self.outname)#
            print(self.dt)


Handling("/home/mirza/Documents/Indonesia Bangkit/source/2021.csv", "/home/mirza/Documents/Indonesia Bangkit/source/2020.csv")



