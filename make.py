import pandas as pd

dt = pd.read_csv(r"C:\Users\ramad\OneDrive\Dokumen\Code\Indonesia Bangkit\source\2021.csv", dtype=str)
# menghapus kolom Tahunan, Wilayah, _id
del dt['Tahunan']
del dt['Wilayah Kereta Api']
del dt['_id']
print(dt)
print("\n================================")

dt = dt.iloc[2] # mengambil data dari wilayah jawa
dt = pd.DataFrame(dt)
print(dt)
print("\n================================")

dt[''] = [i for i in range(1,13)] # membuat kolom baru untuk dijadikan format index
dt = dt.set_index('')
print(dt)
print("\n================================")

dt.insert(0, 'bulan', [i for i in range(1,13)]) # membuat kolom 'bulan' sebagai pertama
print(dt)
print("\n================================")

dt.columns =['bulan', 'jumlah'] # merename semua kolom


print(dt)
#dt.to_csv('dt2021.csv')



