# GBSIM PocketBeagle Techlab Cape Examples
Simple Examples for trying out Mikroe Click Boards on Techlab Cape through greybus Simulator

## OLED C Click Example

This example has an OLED C Click plugged into the Mikrobus Slot of the Techlab Cape and Displays a slideshow images on the OLED C Screen, the buttons(L and R) on the Techlab Cape can be used to change the currently displayed image.

### Running the example

Connect the OLED C Click to the Techlab Cape Mikrobus Slot, then start the GBSIM(greybus simulator) by running the following command :

``` sudo startgbsim```

Now using the insclick CLI Utility the OLED C Click can be loaded using the command :

``` sudo insclick oledc p1```

If the setup was successful, random text and a blinking cursor will be displayed on the OLED screen, now run the examples using the following commands:

``` 
cd oledc
python main.py
```

Now on pressing the buttons(L and R) on the Techlab Cape should display different images on the display. For more information about the code, see a similar project here : https://beagleboard.org/p/103416/standalone-magic-8-ball-pocketbeagle-mikro-click-boards-4f1bb4

To change the images being displayed, the images img*.jpg on the oledc/ directory can be replaced with your images, please note that the oledc screen has an usable size of 96px X 96px and the images has to be resized to that particular size.

## OLED B Click Example

This example has an OLED B Click plugged into the Mikrobus Slot of the Techlab Cape and continously Displays the light intensity level measured by the Light Sensor in the Techlab Cape to the OLED Display.

### Running the example

Connect the OLED B Click to the Techlab Cape Mikrobus Slot, then start the GBSIM(greybus simulator) by running the following command :

``` sudo startgbsim```

Now using the insclick CLI Utility the OLED C Click can be loaded using the command :

``` sudo insclick oledb p1```

If the setup was successful, 'debian 1' and a blinking cursor will be displayed on the OLED screen, now run the examples using the following commands:

``` 
cd oledb
sudo python main.py
```

Now on changing the light intensity level received by the sensor , the corresponding reading on the OLED display will change accordingly.

## RTC 6 Click Example

This example has an RTC 6 Click plugged into the Mikrobus Slot of the Techlab Cape and continously Displays the current time obtained from the RTC to the LED 7 Segment Displays on the Techlab Cape , as there are not enough 7-seg displays available to display the time simultaneously, the example first displays Hours for 2 times, then minutes and then seconds.

### Running the example

Connect the RTC 6 Click to the Techlab Cape Mikrobus Slot, then start the GBSIM(greybus simulator) by running the following command :

``` sudo startgbsim```

Now using the insclick CLI Utility the RTC6 Click can be loaded using the command :

``` sudo insclick rtc6 p1```
now run the examples using the following commands:

``` 
cd rtc
sudo python main.py
```

Now the current time will be displayed on the 7-seg led displays on the cape continously.

