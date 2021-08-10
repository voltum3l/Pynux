import subprocess
import os

def GetMyIp():

	subprocess.call("ifconfig > temp.txt", shell=True)

	archive=open("temp.txt","r")
	string=archive.read()

	ipv4=""

	limitLeft=string.find("inet ") + 5
	limitRight=string.find("netmask")
	indexer=limitLeft

	for i in range(limitRight - limitLeft):
		if string[indexer] != " ":
			ipv4+=string[indexer]
		indexer +=1

	archive.close()
	os.remove("temp.txt")
	return int(ipv4)

