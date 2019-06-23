import os
import time

os.system("sudo ./display.sh "+ r"\\x40 " +r"\\x00 " + r"\\x00")
os.system("sudo ./display.sh "+ r"\\x40 " +r"\\x01 " + r"\\x00")

def writenumber(num):
    if(num>99):
        return
    dig1=num%10
    dig2=num/10
    hex1=gethex(dig1)
    hex2=gethex(dig2)
    os.system("sudo ./display.sh "+ r"\\x40 " +r"\\x12 " + hex2)
    os.system("sudo ./display.sh "+ r"\\x40 " +r"\\x13 " + hex1)

def clearseg():
    os.system("sudo ./display.sh "+ r"\\x40 " +r"\\x12 " + r"\\xff")
    os.system("sudo ./display.sh "+ r"\\x40 " +r"\\x13 " + r"\\xff")

def gettime():
    with open("/sys/class/rtc/rtc1/time", "r") as rtc_file:
        currenttime = rtc_file.readline()
        return currenttime.split(":")

def gethex(digit):
    if(digit==0):
        return r"\\x40"
    elif(digit==1):
        return r"\\xf9"
    elif(digit==2):
        return r"\\x24"
    elif(digit==3):
        return r"\\x30"
    elif(digit==4):
        return r"\\x19"
    elif(digit==5):
        return r"\\x12"
    elif(digit==6):
        return r"\\x02"
    elif(digit==7):
        return r"\\xf8"
    elif(digit==8):
        return r"\\x00"
    elif(digit==9):
        return r"\\x10"

while True:
    clearseg()
    timenow=gettime()
    writenumber(int(timenow[0]))
    time.sleep(0.2)
    clearseg()
    writenumber(int(timenow[0]))
    time.sleep(0.3)
    clearseg()
    writenumber(int(timenow[1]))
    time.sleep(0.3)
    clearseg()
    writenumber(int(timenow[2]))
    time.sleep(0.3)
