import csv
from os import sep
import unidecode
import pandas as pd

path = ''
file = open(path + "amajambo.csv")
csvreader = csv.reader(file)

rows = []
for row in csvreader:
    rows.append(row)

flat_list = []
for sublist in rows:
    for item in sublist:
        flat_list.append(item)

words_list = [item.upper() for item in flat_list]

bad_chars = ['!', "-"]

for i in range(len(words_list)):
    # remove ascents
    words_list[i] = unidecode.unidecode(words_list[i])
    words_list[i] = ''.join((filter(lambda i: i not in bad_chars, words_list[i])))

#save all clean words in csv file
with open('amajambo_cleanedV1.csv', 'w', newline='') as f:
  csv_out = csv.writer(f)
  csv_out.writerows([words_list[index]] for index in range(0, len(words_list)))

#count number of words in our list
def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

print("Number of elements in the entire list: ", get_number_of_elements(words_list))

#letters_count = [len(i) for i in words_list]

#print(letters_count)

# find words with only 5 letters
def five_letter(words):
    new_wordlist = []
    for item in words:
        if len(item) == 5:
            new_wordlist += [item]
    return new_wordlist 

res = five_letter(words_list)

print("Number of elements in our new list of 5 letter words: ", get_number_of_elements(res))
#save all clean words in csv file
with open('amajambo_5letters.csv', 'w', newline='') as f:
  csv_out = csv.writer(f)
  csv_out.writerows([res[index]] for index in range(0, len(res)))

