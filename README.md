# python-port-scanner
Basic port scanner built with Python module Socket

Utility for open/closed port scanning on given IP or host name (DNS name transition enabled)

Usage:
type in command line
"python scanner.py <target> <scan mode> <amount of ports to be scanned>"

Scan modes: 
 "-s1" - port response timeout set to 0.1 seconds
 "-s2" - port response timeout set to 0.2 seconds
 "-s3" - port response timeout set to 0.3 seconds
 "-s4" - port response timeout set to 0.4 seconds
 "-s5" - port response timeout set to 0.5 seconds

By default timeout is set to 1 second

Amount of ports to be scanned is integer entered by user as argument. Defines scan range (from 0 to entered value).
By default is set to 5 ports.
