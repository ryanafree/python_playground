import re
import csv

fhand = open('companylist.csv')
fread = csv.reader(fhand)
fdata = list(fread)

for line in fdata:
    if re.search('Nyse', line):
        print('Nyse')
    elif re.search('Nasdaq', line):
        print('Nasdaq')
    else:
        print('Amex')

