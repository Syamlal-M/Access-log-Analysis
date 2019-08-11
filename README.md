#  Log file Analysis using Python

 You can use simple python codes to organize and analyze your access_log file.
 Here I am using logparser module for analyzing access_log file in accordance with different custom conditions.
 
 ## Logparser Module
 
 Logparser module parses a log file in to a proper dictionary, arranged in a systematic manner
Copy the logparser.py file to your current working directory for using the loagparser module
You can download the Logparser file from this [link](https://github.com/Syamlal-M/Access-log-Analysis/blob/master/logparser.py).

### Log line

```
118.24.109.217 - - [30/Mar/2019:00:01:14 +0000] "GET /Drupal.php HTTP/1.1" 404 10086 "-" "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)"

118.24.109.217 - - [30/Mar/2019:00:01:18 +0000] "GET /lang.php?f=1 HTTP/1.1" 404 10086 "-" "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)"

118.24.109.217 - - [30/Mar/2019:00:01:19 +0000] "GET /izom.php HTTP/1.1" 404 10086 "-" "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)"
```

### Processed logparser Output:

 ```bash
 {'host': '118.24.109.217', 'identity': '-', 'user': '-', 'time': '30/Mar/2019:00:01:14 +0000', 'request': 'GET /Drupal.php HTTP/1.1', 'status': '404', 'size': '10086', 'referer': '-', 'agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'}
{'host': '118.24.109.217', 'identity': '-', 'user': '-', 'time': '30/Mar/2019:00:01:18 +0000', 'request': 'GET /lang.php?f=1 HTTP/1.1', 'status': '404', 'size': '10086', 'referer': '-', 'agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'}
{'host': '118.24.109.217', 'identity': '-', 'user': '-', 'time': '30/Mar/2019:00:01:19 +0000', 'request': 'GET /izom.php HTTP/1.1', 'status': '404', 'size': '10086', 'referer': '-', 'agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'}
```
## Task list

- Python code for logparsing an accesslog file
- Python code for listing the number of hits per IP
- Python code for listing the hits per day
- Python code for listing the Hits per IP on the basis of Error code
- Python code for list the IP list of the ERROR code input

### Python code for logparsing an accesslog file
   
   This code will organize the log file as the example provided, which will be more understandable
    
  **You need to update the absolute path of your logfile while declaring file variable**
 
 I have put my access_log in the home directory as I mentioned just the file name in the python code.
  ```python
import logparser
counter = {}
logfile = 'access_log'
with open(logfile,'r') as fh: #read the logs in the file

  for logs in fh:

      output = logparser.parser(logs)
      print(output)
 ```
 
### Python code for listing the number of hits per IP

```Python

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
```

###  Sample Result
   ```python
   
   118.24.109.217: 115
209.17.96.210: 6
188.213.175.168: 1
209.17.96.26:  6
87.7.228.195:  1
162.158.62.81:  1
162.158.62.61:  1
162.158.63.172: 1
64.62.252.174:  854
196.52.43.98:   1
127.0.0.1:   122
```
### Python code for listing the hits per day
    
   This code will list the number of hits per day
   
```python
import logparser
file = 'access_log'
count = {}

with open(file) as fh:
    for line in fh:
        date = logparser.parser(line)["time"].split(':')[0]
        if date in count:
            count[date] += 1
        else:
            count[date] = 1
for time in count:
    hit = count[time]
    print('{} hits on {}'.format(hit,time))
```

### Sample Result
    
```bash
10000 hits on 30/Mar/2019
```

### Python code for listing the Hits per IP on the basis of Error code

```python
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
```
 
 ### Sample Result
 
 ```bash
 ubuntu@/~$ python3  errorstatus.py
404
---

        ::1                  : 1621
        64.62.252.163        : 3501
401
---

200
---

301
---

304
---

403
---
```
