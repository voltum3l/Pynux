import subprocess
import myIp

def returnClass():
	ip=myIp.GetMyIp()
	firstOctet=""
	ipClass=""


	for i in range(len(ip)):
		if ip[i] != ".":
			firstOctet += ip[i]
		else:
			break
	firstOctet=int(firstOctet)

	if firstOctet < 128:
		ipClass="A"
	if firstOctet < 192 and firstOctet > 127:
		ipClass="B"
	if firstOctet < 224 and firstOctet > 191:
		ipClass="C"
	if firstOctet < 240 and firstOctet > 223:
		ipClass="D"
	if firstOctet >= 240 and firstOctet > 239:
		ipClass="E"

	return ipClass
