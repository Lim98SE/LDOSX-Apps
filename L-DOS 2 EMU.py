# L-DOS 2.0 Script

import os
import winsound
import webbrowser
import psutil
import time
#declare common libraries
from lxml import html
import requests
import urllib.request
import ctypes
import sys
#declare update libraries
i = open("info.txt")
x = i.readlines(1)
y = i.readlines(2)
vnum = int(x[0])
vstr = str(y[0])
run = False
pd = os.getcwd()
#declare system variables
print("Welcome to L-DOS " + vstr + "!")
#boot message
print("Checking for updates...")
#update code below
tst = requests.get("https://lucid-meitner-d7a4e1.netlify.app/update.html", timeout=5)
if tst:
    page = requests.get("https://lucid-meitner-d7a4e1.netlify.app/update.html")
    tree = html.fromstring(page.content)
    req = tree.xpath('//p[@class="req"]/text()')
    num = tree.xpath('//p[@class="num"]/text()')
    ver = tree.xpath('//p[@class="ver"]/text()')
    a = str(req[0])
    b = str(num[0])
    c = int(ver[0])
    req = a
    num = b
    ver = c
    print(req + ", " + num + ", " + str(ver))
    if int(req) == 1 and vnum < c:
        #checks if update is required
        page = requests.get("https://lucid-meitner-d7a4e1.netlify.app/dlup.html")
        url = "https://lucid-meitner-d7a4e1.netlify.app/nv.py"
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        urllib.request.urlretrieve(url, os.getcwd())
        run = True
        i.close()
        i = open("info.txt", "w")
        newinfo = a + "\n" + b + "\n" + str(c)
        i.write(newinfo)
        i.close()
        i = open("info.txt", "r")
    else:
        print("You're up to date.")
else:
    print("Could not access update service.")
print("Now loading L-DOS.")
#finish update
if run:
    #checks if an update happened, if so, display changelog
    page = requests.get("https://lucid-meitner-d7a4e1.netlify.app/info.html")
    tree = html.fromstring(page.content)
    info = tree.xpath('//p[@class="info"]/text()')
    for i in info:
        print(i)
cmd = os.getcwd()[0:3]
while 1 == 1:
    command = input(cmd)
    if command == "break":
        exit()
    elif "echo " in command:
        print(":" + command[4:len(command)])
    elif "ping " in command:
        url = command[5:len(command)]
        print(": " + url)
        ping = requests.get("http://" + url, timeout=1)
        if not ping:
            print("Didn't connect to http.")
            break
        else:
            print("Connected successfully to http.")
        ping = requests.get("https://" + url, timeout=1)
        if not ping:
            print("Didn't connect to https.")
            break
        else:
            print("Connected successfully to https.")
    elif command in os.listdir():
        if input("Open with L-DOS tool? Y/N: ").lower() == "y":
            if ".txt" in command:
                o = open(command)
                print(o.read())
                o.close()
        else:
            webbrowser.open(command)
    elif command == "dir":
        for x in os.listdir():
            print(x)
    elif "dirs " in command:
        term = command[5:len(command)]
        a = 0
        for x in os.listdir():
            if term in x:
                print(x)
                a = a + 1
        if a == 0:
            print("No results found.")
    elif "cd " in command:
        cdto = command[3:len(command)]
        if os.path.exists(cdto):
            pd = os.getcwd()
            os.chdir(cdto)
        else:
            print("Directory not found.")
    elif command == "pd":
        os.chdir(pd)
    elif "new " in command:
        fn = command[4:len(command)]
        f = open(fn, "w")
        f.close()
        webbrowser.open(fn)
    elif command == "backup":
        print("Backing up L-DOS to bk.py")
        f = open("bk.py", "w")
        z = open("L-DOS.py", "r")
        f.write(z.read())
        f.close()
        z.close()
    elif command == "chkdsk":
        disk = psutil.disk_usage("/")
        print("CHKDSK Finished.")
        print(str(round(disk.total / 2**30, ndigits=2)) + "GB Total")
        print(str(round(disk.used / 2**30, ndigits=2)) + "GB Used")
        print(str(round(disk.free / 2**30, ndigits=2)) + "GB Free")
    elif command == "cls" or command == "command":
        for i in range(50):
            print("\n")
    elif "copy " in command:
        fn = command[5:len(command)]
        f = open(fn, "r")
        ext = command.find(".", 0, len(command))
        z = open("Copied File" + command[ext:len(command)], "w")
        z.write(f.read())
        f.close()
        z.close()
        print("Copied " + fn + " to \"Copied File\".")
    elif "del " in command:
        fn = command[3:len(command)]
        os.remove(fn)
    elif "findstr " in command:
        split = command.find(" ", 8, len(command))
        term = command[8:int(split)]
        file = command[int(split + 1):len(command)]
        f = open(file)
        for i in f.readlines():
            if term in i:
                print(i)
    elif "md " in command:
        os.mkdir(command[3:len(command)])
    elif "mkdir " in command:
        os.mkdir(command[6:len(command)])
    elif command == "help":
        page = requests.get("https://lucid-meitner-d7a4e1.netlify.app/info.html")
        tree = html.fromstring(page.content)
        info = tree.xpath('//p[@class="help"]/text()')
        for i in info:
            print(i)
    else:
        print("Error! Command not found.")
    winsound.Beep(1000, 250)
