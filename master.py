import time
import subprocess
import createLogFile
import readProxy

bleConVal = subprocess.check_output("hcitool con",shell = True)
Address = bleConVal.splitlines()
if len(Address) > 1:
	for n in range(len(Address)):
		bleAddr = Address[1].strip()
		bleAddr = bleAddr.strip('>')
else:
	bleAddr = "no bluetooth devices found"

irVal = str(readProxy.main())
#irVal = irVal.strip('(,)')

createLogFile.main(bleAddr, irVal)

