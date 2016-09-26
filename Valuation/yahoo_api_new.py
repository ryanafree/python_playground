import requests
import csv
import time

file = open('tickers_samp.csv', newline='')
header = open('headers.txt')
output_file = open('output.csv', 'a', newline='')

data = csv.reader(file)

output_writer = csv.writer(output_file)
output_writer.writerow(header)


def yahoo_csv():
    for ticker in data:
        url = 'http://finance.yahoo.com/d/quotes.csv?s={0}&f=nsj1p1edyrp5p6b4r5a2f6s7kje7e8r6r7&e=.csv'.format(ticker)
        with requests.Session() as s:
            download = s.get(url)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines())
            crf = ''.join(cr)
            output_writer.writerow(crf)
            time.sleep(.3)


yahoo_csv()
