import subprocess
import os

def returnRouterIp():
	subprocess.call("ip route | grep default > temp.txt", shell=True)
	archive=open("temp.txt","r")
	string=archive.read()

	routerIp=""
	limitLeft=string.find("default via ") + 12
	limitRight=string.find("dev")
	indexer=limitLeft
	for i in range(limitRight - limitLeft):
		if string[indexer] != " ":
			routerIp+=string[indexer]
		indexer +=1

	archive.close()
	os.remove("temp.txt")
	return routerIp
