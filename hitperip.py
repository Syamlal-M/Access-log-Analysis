import logparser
File = 'access_log'
counter = {}

with open(File,'r') as fh:
    for line in fh:
        ip = logparser.parser(line)['host']
        if ip in counter:
            counter[ip] += 1
        else:
            counter[ip] = 1
for ip in counter:
    hit = counter[ip]
    print('{}:{:15}'.format(ip,hit))
