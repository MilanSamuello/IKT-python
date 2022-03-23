#!/usr/bin/python3
from tkinter import *
class SimpleGUI:
    def __init__(self, master):
        self.master = master
        master.title('Simple GUI')
        
self.labelName = Label(master, text='Name')
self.labelName.grid(row=1, column=1)
self.name = Entry(master)
self.name.grid(row=1, column=5)
# main
master = Tk() # creates an instance of GUI
SimpleGUI(master)
master.mainloop() # makes the graphics window stay up

