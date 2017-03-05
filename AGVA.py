#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
from Tkinter import *
from auth import get_credentials

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        
        var1 = StringVar()
        label1 = Tkinter.Label(self, textvariable=var1, justify='left',font=("Arial", 18), bg="#ffc107", pady=15)
        var1.set("Welcome to Automated Gmail Virtual Assistant ")

        var2 = StringVar()
        label2 = Tkinter.Label(self,textvariable=var2,justify='center',font=("Arial", 12),fg="black", bg="white")
        var2.set("Program name: AGVA.py \n Publisher: IIT Jodhpur \n File origin: Hard drive on this computer")

        var3 = StringVar()
        label3 = Tkinter.Label(self, textvariable=var3, font=("Arial", 12), bg="#bdbdbd")
        var3.set("We will keep track of your mails  ")

        var4 = StringVar()
        label4 = Tkinter.Label(self, textvariable=var4,justify='center',font=("Arial", 15),fg="black", bg="#bdbdbd")
        var4.set("    Do you want to start the software?")

        label7 = Tkinter.Label(self, text="\n", bg="#bdbdbd")
        label8 = Tkinter.Label(self, text="\n", bg="white")
        label9 = Tkinter.Label(self, text="\n", bg="white")

        button1 = Tkinter.Button(self,text=u"Yes", fg="#a1dbcd", bg="#383a39", command = self.start_the_world)
        button2 = Tkinter.Button(self,text=u"Exit", fg="#a1dbcd", bg="#383a39", command = self.exit_the_world)

        label1.grid(row=0, column=0,columnspan=15,sticky='EW')
        label2.grid(row=2, column=0,columnspan=15,sticky='EW')
        label3.grid(row=4, column=0,columnspan=15,sticky='EW')
        label4.grid(row=5, column=0,columnspan=15,sticky='EW')
        label7.grid(row=6, column=0,columnspan=15,sticky='EW')
        label8.grid(row=1, column=0,columnspan=15,sticky='EW')
        label9.grid(row=3, column=0,columnspan=15,sticky='EW')
        button1.grid(row=7, column=5)
        button2.grid(row=7, column=10)

    def start_the_world(self):
        cred = get_credentials()
        global app
        app.quit()

    def exit_the_world(self):
        global app
        app.quit()
              

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Automated Gmail Virtual Assistant')
    app.geometry("505x310")
    app.configure(bg="#bdbdbd")
    app.resizable(width='FALSE', height='FALSE')
    app.mainloop()


