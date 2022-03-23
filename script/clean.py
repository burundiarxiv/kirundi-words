import csv
from operator import ne
from os import sep
import unidecode
import pandas as pd
import itertools
import ast

path = ''
file = open(path + "amajambo.csv")
csvreader = csv.reader(file)

#file to merge
new_file = open(path + "amajambo_6.txt", "r")
linesreader = new_file.read()

# Converting string to list
lines = ast.literal_eval(linesreader)

#output files
f1 = open('amajambo_cleanedV1.csv', 'w', newline='')
f2 = open('amajambo_6.csv', 'w', newline='')

rows = []
for row in csvreader:
    rows.append(row)

flat_list = []
for sublist in rows:
    for item in sublist:
        flat_list.append(item)

words_list = [item.lower() for item in flat_list]

bad_chars = ['!', "-"]
for i in range(len(words_list)):
    # remove ascents
    words_list[i] = unidecode.unidecode(words_list[i])
    words_list[i] = ''.join((filter(lambda i: i not in bad_chars, words_list[i])))

#save all clean words in csv file
with f1:
    csv_out1 = csv.writer(f1)
    csv_out1.writerows([words_list[index]] for index in range(0, len(words_list)))

#count number of words in our list
def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

print("Number of elements in the entire list: ", get_number_of_elements(words_list))
print("Number of elements in the list to merge: ", get_number_of_elements(lines))

# find words with only specific number of letters
def five_letter(words):
    new_wordlist = []
    for item in words:
        if len(item) == 6:
            new_wordlist += [item]
    return new_wordlist 

res = five_letter(words_list)

res2 = res.copy()
for w in lines:
    res2.append(w)

print("Number of elements in our new list of words extracted from amajambo: ", get_number_of_elements(res))
print("Number of elements in the merged list: ", get_number_of_elements(res2))
#save all clean words in csv file
with f2:
    csv_out2 = csv.writer(f2)
    csv_out2.writerows([res2[index]] for index in range(0, len(res2)))




