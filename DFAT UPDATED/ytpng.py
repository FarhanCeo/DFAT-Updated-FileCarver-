import os
curdir = os.getcwd()
print(curdir)
def png(drive):
    #drive = "\\\\.\\H:"     # Open drive as raw bytes
    fileD = open(drive, "rb")
    size = 512              # Size of bytes to read
    byte = fileD.read(size) # Read 'size' bytes
    offs = 0                # Offset location
    drec = False            # Recovery mode
    rcvd = 0                # Recovered file ID
    while byte:
        #file signature of png is 89 50 4E 47 0D 0A 1A 0A
        found = byte.find(b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a')#89 50 4E 47 0D 0A 1A 0A
        if found >= 0:
            drec = True
            print('==== Found png at location: ' + str(hex(found+(size*offs))) + ' ====')
            # Now lets create recovered file and search for ending signature
            
                
            os.chdir(curdir+"\\PNGFILES")    
            fileN = open(str(rcvd) + '.png', "wb")
            fileN.write(byte[found:])
            while drec:
                byte = fileD.read(size)
                bfind = byte.find(b'\x49\x45\x4e\x44\xae\x42\x60\x82')#49 45 4E 44 AE 42 60 82
                if bfind >= 0:
                    fileN.write(byte[:bfind+8])
                    fileD.seek((offs+1)*size)
                    print('==== Wrote png to location: ' + str(rcvd) + '.png ====\n')
                    drec = False
                    rcvd += 1
                    fileN.close()
                else: fileN.write(byte)
        byte = fileD.read(size)
        offs += 1
    fileD.close()
    