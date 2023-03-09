import os
curdir = os.getcwd()
def html(drive):
    #drive = "\\\\.\\H:"     # Open drive as raw bytes
    fileD = open(drive, "rb")
    size = 512              # Size of bytes to read
    byte = fileD.read(size) # Read 'size' bytes
    offs = 0                # Offset location
    drec = False            # Recovery mode
    rcvd = 0                # Recovered file ID
    while byte:
        #file signature of html is \x3C\x68\x74\x6D\x6C
        found = byte.find(b'\x3C\x68\x74\x6D\x6C')
        if found >= 0:
            drec = True
            print('==== Found html at location: ' + str(hex(found+(size*offs))) + ' ====')
            # Now lets create recovered file and search for ending signature
            os.chdir(curdir+"\\HTMLFILES")
            fileN = open(str(rcvd) + '.html', "wb")
            fileN.write(byte[found:])
            while drec:
                byte = fileD.read(size)
                bfind = byte.find(b'\x2F\x68\x74\x6D\x6C\x3E')
                if bfind >= 0:
                    fileN.write(byte[:bfind+8])
                    fileD.seek((offs+1)*size)
                    print('==== Wrote png to location: ' + str(rcvd) + '.html ====\n')
                    drec = False
                    rcvd += 1
                    fileN.close()
                else: fileN.write(byte)
        byte = fileD.read(size)
        offs += 1
    fileD.close()