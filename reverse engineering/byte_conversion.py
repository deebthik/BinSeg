#script used to convert binary file to decimal file (4 bytes/line)
import sys
import os
arr = os.listdir('/Users/aizazansari/Desktop/Uni Data/MOMA/armhf')

for elem in arr:
    
    read_file_path = 'armhf/' + each
    
    with open(read_file_path, mode='rb') as file: # b -> binary
        
        #counter to write 4 bytes on each line
        count = 1
        wrie_file_path = "armhf/" + elem + ".txt"
        write_file = open(wrie_file_path,"w")
        
        while 1:
            
            byte_s = file.read(1)
            
            if count%4 == 0:
                value = int.from_bytes(byte_s, byteorder=sys.byteorder)
                write_file.write(str(value)+ "\n")
                
            else:
                value = int.from_bytes(byte_s, byteorder=sys.byteorder)
                write_file.write(str(value)+ " ")
                
            count = count + 1
            
            #eof reached
            if not byte_s:
                break

    write_file.close()   