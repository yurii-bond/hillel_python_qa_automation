import csv


with open('config.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row)
#
# data = [
#     ['Name', 'Age', 'City']
#     , ['John', '25', 'New York']
#     , ['Alice', '32', 'London']
#     , ['Bob', '40', 'Paris']
#     ,
# ]
#
# with open('output.csv', 'w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(data)

