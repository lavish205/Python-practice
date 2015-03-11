import redis
import csv
import re
import os

cRedis = redis.Redis()

c = csv.reader(open("example.csv", "rb"))

for row in c:
    cRedis.hmset(row[3], {'name': row[1]+' '+row[2], 'email': row[4], 'college': row[5], 'number': row[3]})

clear = lambda: os.system('clear')


def crawl(pat):
    number = cRedis.keys(pat+'*')
    if not (number == []):
        for r in number:
            result = cRedis.hmget(r, ['name', 'email', 'number', 'college'])
            clear()
            print '\nName: ' + result[0] + '\nEmail: ' + result[1] + \
                  '\nMobile: ' + result[2] + '\nCollege: ' + result[3]

    else:
        clear()
        print "No result found"


while True:
    pattern = raw_input('Number: ')
    if len(pattern) >= 3:
        num_format = re.compile("^[1-9][0-9]*\.?[0-9]*")
        isNumber = re.match(num_format, pattern)
        if isNumber:
            crawl(pattern)
        else:
            clear()
            print "Make Sense?"

    else:
        clear()
        print "Characters should be equal or more than 3"
