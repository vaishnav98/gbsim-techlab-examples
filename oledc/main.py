import time
import os

# configure the buttons on Techlab Cape as GPIO
os.system("config-pin p1.29 gpio")
os.system("config-pin p2.33 gpio")

choice=0
prevchoice=0

def show(mychoice):
    image_choices = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg', 'img5.jpg', 'img6.jpg', 'img7.jpg', 'img8.jpg', 'img9.jpg', 'img10.jpg', 'img11.jpg', 'img12.jpg', 'img13.jpg', 'img14.jpg', 'img15.jpg']
    command = 'sudo ./display.sh ' + image_choices[mychoice]
    os.system(command)

while True:
    time.sleep(0.01)
    with open('/sys/class/gpio/gpio45/value', 'r') as infile:
        buttonl=int(infile.readline())
    with open('/sys/class/gpio/gpio117/value', 'r') as infile:
        buttonr=int(infile.readline())
    if(not(buttonr) and (choice < 14)):
        choice+=1
    elif((not buttonl) and (choice > 0)):
        choice-=1
    if(choice != prevchoice):
	show(choice)
    prevchoice=choice

