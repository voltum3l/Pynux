import subprocess
import os
from tcolors import *


def isRoot():
	subprocess.call("id -u > temp.txt",shell=True)
	arch=open("temp.txt","r")
	string=arch.read()
	root=False

	if int(string) == 0:
		print(tcolors.OK + "[*] El user tiene privilegios ROOT. Puede seguir el proceso." + tcolors.RESET)
		root=True
	else:
		print(tcolors.FAIL + "[*][*]  El user no tiene privilegios ROOT. Acceda como ROOT y vuelva a iniciar el programa." + tcolors.RESET)
		root=False

	return root