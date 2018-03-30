"""Parse log entries for datetimes and calculate the time
   between two shutdown initializations"""
from datetime import datetime
from datetime import timedelta
import os
import urllib.request


def read_file(tempfile):
    """Read in tempfile return list of lines"""
    with open(tempfile, 'r') as f:
        lines = f.readlines()
    return lines

def convert_to_datetime(line):
    """Given a line extract timestamp and convert to datetime"""
    ld = line.split(" ")
    dtstamp = ld[1]

    sec = int(dtstamp[11:13]) * 3600 + int(dtstamp[14:16]) * 60 + int(dtstamp[17:19])

    dtstamp = datetime(int(dtstamp[0:4]),
                       int(dtstamp[5:7]),
                       int(dtstamp[8:10]),
                       int(dtstamp[11:13]),
                       int(dtstamp[14:16]),
                       int(dtstamp[17:19])
                       )

    return dtstamp


def time_between_shutdowns(lines):
    """Extract shutdown init events and calculate timedelta between
       first and last one"""
    t = lines[1] - lines[0]
    return timedelta(t.days, t.seconds)

# prep
cwd = os.getcwd()
tempfile = os.path.join(cwd, 'log.log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', tempfile)

# code
lines = read_file(tempfile)

dts = []
for l in lines:
    if "Shutdown initiated" in l:
        dt = convert_to_datetime(l)
        dts.append(dt)


td = time_between_shutdowns(dts)
print("Time between shutdowns {0}".format(td))




