import socket
import sys


for port in range(1, 1025):
    sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout (1)
    result = sock.connect_ex (("192.168.48.1", port))
    if 0 == result :
        print ("Port : {} Open".format (port))
        sock.close ()

from datetime import datetime
startTimestamp = datetime.now()

f = open("Scan-report.txt", 'w')
print("-"*60, file=f)
print("Scanning host:", server, file=f)
print("-"*60, file=f)
print(startTimestamp, file=f)

import time
start = time.time()

except KeyboardInterrupt:
    print(" ERROR OCCURRED !! Scan was aborted by user.", file=f)
    sys.exit()

except socket.gaierror:
    print("Host name could not be resolved. Exiting Scan.", file=f)
    sys.exit()

except socket.error:
    print("Could not connect to server", file=f)
    sys.exit()

endTimestamp = datetime.now()
print(endTimestamp, file=f)

print("Scan finished in", time.time() - start, "seconds.", file=f)