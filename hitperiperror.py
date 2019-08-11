import logparser
statuscounter = {}
logfile = 'access_log'
with open(logfile,'r') as fh: #read the logs in the file

    for logs in fh:

        output = logparser.parser(logs)
        ip = output['host']
        status = output['status']
        if status not in statuscounter:  #Creating a dict with key status and value IP addresses.

            statuscounter[status] = []
            statuscounter[status].append(ip)
        else:
            statuscounter[status].append(ip)

for status in statuscounter: #Generating Result From the statusCounter


    ipCounter = {}

    for ip in statuscounter[status]:

        if ip not in ipCounter:

            ipCounter[ip] = 1
        else:

            ipCounter[ip] += 1

    print(status)
    print('-' * len(status))
    print()

    for ip in ipCounter:
        hit = ipCounter[ip]
        if hit >= 1000:
            print('\t{:20} : {}'.format(ip,hit))
