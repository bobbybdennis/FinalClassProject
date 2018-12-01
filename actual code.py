import shell_command
import subprocess
import os
import datetime

from shell_command import shell_call
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Command Buddy")
window.geometry("100x100")
window.configure(background='light blue')


def Hostname():
   shell_call("hostname & hostname >> Results.txt ")
#def Hostname1():
#    shell_call("hostname >> Results.txt")
window.geometry("275x175")
def GetMac():
    shell_call("getmac & getmac >> Results.txt")
def Ping():
    shell_call("Ping www.google.com & Ping www.google.com >> Results.txt")
def GetIP():
    shell_call("ipconfig & ipconfig >> results.txt")
def FlushDNS():
    shell_call("ipconfig /flushdns & ipconfig /flushdns >> Results.txt")
def ScanNow():
    shell_call("sfc /scannow")
def TaskList():
    shell_call("tasklist & tasklist >> Results.txt")
def StarWars():
    shell_call("telnet towel.blinkenlights.nl")
def PowerSave():
    shell_call("powercfg/energy & powercfg/energy >> Results.txt")
def Date():
    shell_call("date /t & time /t & date /t >> Results.txt & time /t >> Results.txt")
#def ST1():         <-------- figure this out later. much later. maybe never
    #cmd = 'python myprog.py 21 --mass 4'
   # failure = subprocess.call(cmd, shell=True)

    #os.system("start cmd")
B1 = Button(window, text = "What is my Hostname?", command = Hostname)
B1.place(x = 0,y = 0)
B2 = Button(window, text = "Internet connectivity", command = Ping)
B2.place(x = 0, y = 45)
B3 = Button(window, text = "MAC address?", command = GetMac)
B3.place(x = 0, y = 90)
B4 = Button(window, text = "My IP address?", command = GetIP)
B4.place(x = 150, y = 0)
B5 = Button(window, text = "Flush DNS", command = FlushDNS)
B5.place(x = 150, y = 45)
B6 = Button(window, text = "Task list", command = TaskList)
B6.place(x = 150, y = 90)
B7 = Button(window, text = "Date and Time", command = Date)
B7.place(x = 150, y = 130)
#B8 = Button(window, text = "Starwars part 1", command = ST1)
#B8.place(x = 50, y = 450)
#B9 = Button(window, text = "ipconfig", command = GetIP)
#B9.place(x = 50, y = 450)
window.mainloop()
