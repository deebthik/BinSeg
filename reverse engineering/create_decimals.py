#script used to reverse engineer binary and write disassembly to csv file
import idc
import idautils
import idaapi
idaapi.autoWait()
file_name = "C:\\Users\\user\\Downloads\\decimal_files\\decimal.csv"

#used to generate incremental filename
if os.path.isfile(file_name):
    expand = 1
    while True:
        expand += 1
        new_file_name = file_name.split(".csv")[0] + str(expand) + ".csv"
        if os.path.isfile(new_file_name):
            continue
        else:
            file_name = new_file_name
            break

file = open(file_name,'w')

#appending all segments and their address ranges
all_segments = []
for s in idautils.Segments():
	all_segments.append([s,idc.SegName(s)])
i = 0

#selecting segments which are code or data
segments = []
while i<(len(all_segments)-1):
	if idc.isCode(idc.GetFlags(all_segments[i][0])) or idc.isData(idc.GetFlags(all_segments[i][0])):
		segments.append([all_segments[i][0],all_segments[i+1][0]])
	i = i + 1


string = "address|type|disassembly|bytes"
#iterating over every segment to write address,type,disassembly,bytes to csv file
for segment in segments:
	for address in range(segment[0],segment[1]):
		if idc.isCode(idc.GetFlags(address)):
			string = string + "\n"
			file.write(string)
			print(string) 
			string = str(address) + "|code|" + idc.GetDisasm(address) + "|" + str(idc.Byte(address)) 
		elif idc.isData(idc.GetFlags(address)):
			string = string + "\n"
			print(string)
			file.write(string)
			string = str(address) + "|data|" + idc.GetDisasm(address) + "|" + str(idc.Byte(address)) 
		elif idc.isTail(idc.GetFlags(address)):
			string = string + "-" + str(idc.Byte(address))
idc.Exit(0)
file.close()

