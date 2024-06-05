import pandas as pd

# Membaca data dari file CSV
df = pd.read_csv('data_penjualan.csv')

# Menampilkan beberapa baris pertama dari DataFrame
print(df.head())
