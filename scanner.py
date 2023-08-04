import sys
import socket
from datetime import datetime

#Global variables
port_counter = 0
open_counter = 0

elapsed_time = 0
start_time = 0
end_time = 0

s_state = ""
s_service= ""
s_os = ""

user_scan_timeout = 1
user_port_range_start = 0
user_port_range_end = 5

start_time = datetime.now()

#Extracting arguments
target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4, DNS translation

if len(sys.argv) > 2 and type(sys.argv[2]) == str:
    match sys.argv[2]:
        case "-sF":
            user_scan_timeout = 0.1
        case "-sM":
            user_scan_timeout = 0.5
        case _:
            if len(sys.argv) > 2:
                split = sys.argv[2].split('-s')
                user_scan_timeout = int(split[1])
            else:
                user_scan_timeout = 1
else:
    user_scan_timeout = 1

if len(sys.argv) > 3 or type(sys.argv[2]) != str and sys.argv[3] != "-a":
    user_port_range_end = sys.argv[3]
elif sys.argv[3] == "-a":
    user_port_range_end = 65535
elif type(sys.argv[3])==str and sys.argv[3] != "-a":
    range_split = sys.argv[3].split('-')
    print(range_split)
    user_port_range_start = int(range_split[0])
    user_port_range_end = int(range_split[1])
else:
    user_port_range_start = 0
    user_port_range_end = 5

#Creating header
print("-" * 50)
print("Scanning target " + target)
print(f"Time started: {start_time}")
print("-" * 50)
print("PORT         STATE         SERVICE         OS")

try:
    for port in range(int(user_port_range_start), int(user_port_range_end)):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(user_scan_timeout)
        result = s.connect_ex((target, port))
        port_counter+=1

        #Getting port state
        if result == 0:
            s_state = "open"
            open_counter += 1
        else:
            s_state = "closed"
        #-----------------

        #Getting port OS

        #----------------

        #Getting port service 
        try:  
            protocolname = 'tcp'
            s_service = socket.getservbyport(port, protocolname)
        except:
            pass
        #----------------------
  
        print(f"{port}         {s_state}         {s_service}         {s_os}")

        s.close()

except KeyboardInterrupt:
    print("Ctrl^C Exiting program...")
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print("-" * 50)
    print(f"Time elapsed {elapsed_time}, ports scanned - {port_counter}, open ports found - {open_counter}. Terminating program...")
    print("-" * 50)
    sys.exit()

except socket.gaierror: 
    print("Hostname could not be resolved.")

#Getting elapsed time
end_time = datetime.now()
elapsed_time = end_time - start_time

#Creating footer
print("-" * 50)
print(f"Time elapsed {elapsed_time}, ports scanned - {port_counter}, open ports found - {open_counter}. Terminating program...")
print("-" * 50)