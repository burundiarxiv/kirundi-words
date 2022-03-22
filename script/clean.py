import csv
from os import sep
import unidecode
import pandas as pd

path = '/Users/niyubahweany-arlene/kirundi-words/'
file = open(path + "amajambo.csv")
csvreader = csv.reader(file)

rows = []
for row in csvreader:
    rows.append(row)

flat_list = []
for sublist in rows:
    for item in sublist:
        flat_list.append(item)

words = [item.upper() for item in flat_list]

bad_chars = ['!', "-"]

for i in range(len(words)):
    # remove ascents
    words[i] = unidecode.unidecode(words[i])
    words[i] = ''.join((filter(lambda i: i not in bad_chars, words[i])))

#print(words)

with open('amajambo_cleanedV1.csv', 'w', newline='') as f:
  csv_out = csv.writer(f)
  csv_out.writerows([words[index]] for index in range(0, len(words)))

def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

print("Number of elements in the list: ", get_number_of_elements(words))