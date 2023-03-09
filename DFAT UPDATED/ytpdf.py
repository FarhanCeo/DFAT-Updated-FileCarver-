import os
curdir = os.getcwd()
def pdf(drive):
    #drive = "\\\\.\\H:"     # Open drive as raw bytes
    fileD = open(drive, "rb")
    size = 512              # Size of bytes to read
    byte = fileD.read(size) # Read 'size' bytes
    offs = 0                # Offset location
    drec = False            # Recovery mode
    rcvd = 0                # Recovered file ID
    while byte:
        #file signature of pdf is 25 50 44 46
        found = byte.find(b'\x25\x50\x44\x46')#25 50 44 46
        if found >= 0:
            drec = True
            print('==== Found pdf at location: ' + str(hex(found+(size*offs))) + ' ====')
            # Now lets create recovered file and search for ending signature
            os.chdir(curdir+"\\PDFFILES")
            fileN = open(str(rcvd) + '.pdf', "wb")
            fileN.write(byte[found:])
            while drec:
                byte = fileD.read(size)
                bfind = byte.find(b'\x0a\x25\x25\x45\x4f\x46')#0A 25 25 45 4F 46
                if bfind >= 0:
                    fileN.write(byte[:bfind+6])
                    fileD.seek((offs+1)*size)
                    print('==== Wrote pdf to location: ' + str(rcvd) + '.pdf ====\n')
                    drec = False
                    rcvd += 1
                    fileN.close()
                else: fileN.write(byte)
        byte = fileD.read(size)
        offs += 1
    fileD.close()