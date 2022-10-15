#!python3

from mrjob.job import MRJob
from mrjob.step import MRStep

import csv
import json

#displit dengan menggunakan ,
cols = 'id_customer,name_customer,birthdate_customer,gender_customer,country_customer'.split(',')

def csv_readline(line):
    """Given a sting CSV line, return a list of strings."""
    for row in csv.reader([line]):
        return row

class Jumlahpelangganmemebeli(MRJob):

    def mapper(self, _, line):
        # Convert each line into a dictionary
        row = dict(zip(cols, csv_readline(line)))

        #skip first row as header
        if row['id_customer'] != 'id_customer':
            # Yield the order_date
            yield row['id_customer'],1

    def reducer(self, key, values):
        #for 'order_date' compute
        yield None, (key,sum(values))

if __name__ == '__main__':
    Jumlahpelangganmemebeli.run()

