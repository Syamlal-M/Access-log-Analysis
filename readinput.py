import logparser
counter = {}
logfile = 'access_log'
with open(logfile,'r') as fh: #read the logs in the file

for logs in fh:

    output = logparser.parser(logs)
    print(output)
