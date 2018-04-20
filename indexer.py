'''
convert subnet+ mask to list of start and stop ips


Format of each input addresses file is IP + mask:

10.0.0.1/24
192.168.10.20/30
1.1.1.1/8

etc.

netaddr should handle the subnet calculations, so it doesn't matter if the IP addresses are the network ID.
The output is a TSV file of the first and last IPs available converted into a linear number format, so elementTree can build the interval tree correctly (it can't handle the dotted format)

'''
import netaddr
import os


# ip type object index -1 is the last possible address for the network

outputfilea = open('outputaddressesA.txt' , 'w') 
with open('inputaddressesA.txt' ,'r') as inputfilea:
	for entry in inputfilea:
		ipobj = netaddr.IPNetwork(entry)
		#print(str(ipobj[0]) + '\t' + str(ipobj[-1]))
		ipfirst = ipobj[0]
		iplast = ipobj[-1]
		outputfilea.write(str(ipfirst.value) + '\t' + str(iplast.value) +'\n')
outputfilea.close()


outputfileb = open('outputaddressesB.txt' , 'w') 
with open('inputaddressesB.txt' ,'r') as inputfilea:
	for entry in inputfilea:
		ipobj = netaddr.IPNetwork(entry)
		#print(str(ipobj[0]) + '\t' + str(ipobj[-1]))
		ipfirst = ipobj[0]
		iplast = ipobj[-1]
		outputfileb.write(str(ipfirst.value) + '\t' + str(iplast.value) +'\n')
outputfileb.close()
