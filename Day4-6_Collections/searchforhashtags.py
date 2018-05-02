import csv
import re
from urllib.request import urlretrieve
# Grab table to be parsed


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

t_data = 'https://github.com/pybites/100DaysOfCode/blob/master/LOG.md'
t_csv = 'table.csv'
urlretrieve(t_data, t_csv)

content = []
with open(t_csv) as f:
    content = f.readlines()



