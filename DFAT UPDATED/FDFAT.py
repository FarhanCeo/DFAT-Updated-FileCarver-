import tkinter as tk
from tkinter import *
from tkinter import ttk 
import os
import win32api
import ytjpg as jpg
import ytpdf as pdf
import ytpng as png
import ythtml as html
#import carve
def carve():
    drive=clicked.get()
    label.config(text = "Carving "+drive)
    file = drive[0:-1]
    file = "\\\\.\\"+file
    print(file)
    pdf.pdf(file)
    print("pdf carving completed")
    label.config(text = "Carving "+drive+"20% ")
    jpg.jpg(file)
    print("jpg carving completed")
    label.config(text = "Carving "+drive+"40% ")
    png.png(file)
    print("png carving completed")
    label.config(text = "Carving "+drive+"60% ")
    html.html(file)
    label.config(text = "Carving "+drive+"100% ")
    print("html carving completed")
    
    
    label.config(text = "Carving "+drive+" is completed")
    

H=400   
W=500

#ROOT WINDOW 
root = tk.Tk()
root.title("DFAT") #ASSIGNING THE NAME OF THE WIDGET AS "DFAT"
#change color of root window
root.configure(background='white')
root.geometry(f"{W}x{H}")
root.resizable(0, 0)


#Get all drives
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
no_of_drives = len(drives)

#dropdown list
# datatype of menu text
clicked = StringVar()
# initial menu text
clicked.set( "Select Drive" )
drop = OptionMenu( root , clicked, *drives )
#place the dropdown menu on the root windowd
drop.pack()




# Create button, it will change label text
button = Button( root , text = "Carve" , command = carve ).pack()
  
# Create Label
label = Label( root , text = "Selected Drive " )
label.pack()

print(drives)




root.mainloop()