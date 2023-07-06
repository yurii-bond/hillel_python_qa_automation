import csv
import pandas as pd

file_path = '../lecture_15_16/config.csv'
file_path_2 = '../../../SampleCSVFile_11kb.csv'

fieldnames = ['index', 'product', 'name', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninenth', 'tenth']

# with open(file_path_2, 'r', encoding='cp1252') as file:
#     reader = csv.DictReader(file, fieldnames)
#     for rom in reader:
#         print(rom)

df = pd.read_csv(file_path_2, encoding='cp1252')
print(df)

print('_' * 100)
df_2 = pd.read_csv(file_path)
print(df_2)





