import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
logFile = "/home/adminz/Downloads/python-logparser-accesslog/access.log"

fh = open(logFile) 

ipCounter = {}
for logLine in fh:
    
    clientIp = logLine.split()[0]
    
    if clientIp not in ipCounter:
        
        ipCounter[clientIp] = 1
        
    else:
        
        ipCounter[clientIp] = ipCounter[clientIp] + 1
       
fh.close()

for ip in ipCounter:
    
    hits = ipCounter[ip]
    
    if hits >= 500:
        
        print('{} : {}'.format(ip,hits))

        plt.bar(ip, hits, color=['red', 'red', 'green', 'blue', 'cyan'])
        plt.xticks(rotation=45)
        plt.xlabel('Hits')
        plt.ylabel('IP-Address')
        
