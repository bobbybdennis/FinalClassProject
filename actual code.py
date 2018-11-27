import shell_command
from shell_command import shell_call
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def Hostname():
   shell_call("hostname")
top.geometry("500x500")
def GetMac():
    shell_call("getmac")
def Ping():
    shell_call("Ping www.google.com")
def GetIP():
    shell_call("ipconfig")
def FlushDNS():
    shell_call("ipconfig /flushdns")
def ScanNow():
    shell_call("sfc /scannow")
B1 = Button(top, text = "What is my Hostname?", command = Hostname)
B1.place(x = 35,y = 50)
B2 = Button(top, text = "Check if I can reach the Internet", command = Ping)
B2.place(x = 50, y = 150)
B3 = Button(top, text = "What is my MAC address", command = GetMac)
B3.place(x = 50, y = 300)
B4 = Button(top, text = "What is my IP?", command = GetIP)
B4.place(x = 50, y = 450)
B5 = Button(top, text = "Flush DNS Cache", command = FlushDNS)
B5.place(x = 250, y = 450)
B6 = Button(top, text = "Scan for Problems", command = ScanNow())
B6.place(x = 450, y = 600)
#B7 = Button(top, text = "ipconfig", command = GetIP)
#B7.place(x = 50, y = 450)
#B8 = Button(top, text = "ipconfig", command = GetIP)
#B8.place(x = 50, y = 450)
#B9 = Button(top, text = "ipconfig", command = GetIP)
#B9.place(x = 50, y = 450)
top.mainloop()
