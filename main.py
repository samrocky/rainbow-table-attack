import hashlib
import csv 
from os.path import dirname, join


def sha256(data):
    m = hashlib.sha256()
    m.update(data.encode('utf-8'))
    return m.hexdigest()

dic = {}
for i in range(10000):
    i = '{0:04}'.format(i)
    dic.update({sha256(i):i})

filename = 'passwords.csv'
file = open(join(dirname(__file__), "./{}".format(filename)))


csvreader = csv.reader(file)
namehash = []
for row in csvreader:
    namehash.append(row)

for i in range(0, len(namehash)):
    print("{}-{}".format(namehash[i][0], dic[namehash[i][1]]))
