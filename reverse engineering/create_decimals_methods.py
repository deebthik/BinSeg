#basic approach - not working since it never stops

address = 0

while 1:
	if idc.isCode(idc.GetFlags(address)):
		print "Code", address
	elif idc.isData(idc.GetFlags(address)):
		print "Data", address
	elif idc.isTail(idc.GetFlags(address)):
		print "Tail", address
	elif idc.isHead(idc.GetFlags(address)):
		print "Head", address
	elif idc.isUnknown(idc.GetFlags(address)):
		print "Unknown", address

	else:
		break

	address = address + 1



### faster than previous one - skips over last section however (bug?)

address = 0
if idc.isCode(idc.GetFlags(address)):
		print address

while 1:
	prev_addr = address
	address = idc.FindCode(address, SEARCH_DOWN | SEARCH_NEXT)
	if address == prev_addr:
		break
	else:
		print address


### hybrid approach - works perfectly fine
file = open("combined.txt","w")
all_segments = []
for s in idautils.Segments():
	all_segments.append([s,idc.SegName(s)])
i = 0
selected = ['.init','.plt','.text','.fini','.init_array','.fini_array','.jcr','.got','.data']
segments = []
while i<(len(all_segments)-1):
	if all_segments[i][1] in selected:
		segments.append([all_segments[i][0],all_segments[i+1][0]])
	i = i + 1


string = "address,type,disassembly,bytes"
for segment in segments:
	for address in range(segment[0],segment[1]):
		if idc.isCode(idc.GetFlags(address)):
			string = string + "\n"
			file.write(string) 
			string = str(address) + ",code," + idc.GetDisasm(address) + "," + str(idc.Byte(address)) 
		elif idc.isData(idc.GetFlags(address)):
			string = string + "\n"
			file.write(string)
			print string
			string = str(address) + ",data," + idc.GetDisasm(address) + "," + str(idc.Byte(address)) 
		elif idc.isTail(idc.GetFlags(address)):
			string = string + "-" + str(idc.Byte(address))

file.close()

### hybrid approach - for code only

address = 0
file = open("sample.txt", "w")
if idc.isCode(idc.GetFlags(address)):
		print address, "code", idc.GetDisasm(address), idc.Byte(address)
		file.write(str(address) + ",code," + idc.GetDisasm(address) + "," +  str(idc.Byte(address)) + "\n")
		trail_address = address + 1
		while idc.isTail(idc.GetFlags(trail_address)):
			print trail_address, "tail", idc.GetDisasm(trail_address), idc.Byte(trail_address)
			file.write(str(trail_address) + ",tail," + idc.GetDisasm(trail_address) + "," +  str(idc.Byte(trail_address)) + "\n")
			trail_address = trail_address + 1

while 1:
	prev_addr = address
	address = idc.FindCode(address, SEARCH_DOWN | SEARCH_NEXT)
	if address == prev_addr:
		break
	else:
		print address, "code", idc.GetDisasm(address), idc.Byte(address)
		file.write(str(address) + ",code," + idc.GetDisasm(address) + "," +  str(idc.Byte(address)) + "\n")
		trail_address = address + 1
		while idc.isTail(idc.GetFlags(trail_address)):
			print trail_address, "tail", idc.GetDisasm(trail_address), idc.Byte(trail_address)
			file.write(str(trail_address) + ",tail," + idc.GetDisasm(trail_address) + "," +  str(idc.Byte(trail_address)) + "\n")
			trail_address = trail_address + 1

file.close()

### hybrid approach - for data only

address = 0
file = open("sample-data.txt", "w")
if idc.isData(idc.GetFlags(address)):
		print address, "data", idc.GetDisasm(address), idc.Byte(address)
		file.write(str(address) + ",data," + idc.GetDisasm(address) + "," +  str(idc.Byte(address)) + "\n")
		trail_address = address + 1
		while idc.isTail(idc.GetFlags(trail_address)):
			print trail_address, "tail", idc.GetDisasm(trail_address), idc.Byte(trail_address)
			file.write(str(trail_address) + ",tail," + idc.GetDisasm(trail_address) + "," +  str(idc.Byte(trail_address)) + "\n")
			trail_address = trail_address + 1

while 1:
	prev_addr = address
	address = idc.FindData(address, SEARCH_DOWN | SEARCH_NEXT)
	if address == prev_addr:
		break
	else:
		print address, "data", idc.GetDisasm(address), idc.Byte(address)
		file.write(str(address) + ",data," + idc.GetDisasm(address) + "," +  str(idc.Byte(address)) + "\n")
		trail_address = address + 1
		while idc.isTail(idc.GetFlags(trail_address)):
			print trail_address, "tail", idc.GetDisasm(trail_address), idc.Byte(trail_address)
			file.write(str(trail_address) + ",tail," + idc.GetDisasm(trail_address) + "," +  str(idc.Byte(trail_address)) + "\n")
			trail_address = trail_address + 1

file.close()



