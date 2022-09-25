#script used to run ida in terminal and call the create_decimals script for every arm binary

import subprocess
import os
path = 'C:\\Users\\user\\Downloads\\armhf\\'
python_file = 'C:\\Users\\user\\Downloads\\create_decimals.py'
arr = os.listdir(path)

total = len(arr)
count = 0
for file in arr:
	#skipping over code files since they dont generate content
	#skipping over idb files since ida generates these
	if file.endswith('.code') or file.endswith('.idb'):
		count = count + 1
		print(count,"/",total, "skipped")
		continue

	#added this if condition to skip over files that have already been processed
	if (file+'.idb') in arr:
		count = count + 1
		print(count,"/",total, "skipped, already outputted")
		continue

	#limited file size to 200kb
	if os.stat(path+file).st_size>200000:
		count = count + 1
		print(count,"/",total, "skipped, greatter than 200kb")
		continue

	#call create_decimals.py on file
	print(file)
	command = "ida -A -S" + python_file + " " + path + file
	p = subprocess.Popen(command)
	p.communicate()
	count = count + 1
	print(count,"/",total)

