#### TDSB autofill morning attendance 
Download tdsbautoFill.py file and make the necessary changes. <br />
The main program is well documented and will give you a walkthrough on how to change stuff. <br />
The Selenium Framework library and Python will be require to run this. <br />

Provided you have python3 installed and PyPi (pip) ready to go, follow the next steps to execute this <br />
If you don't have python, install it from here: [Python3](https://www.python.org/downloads/)

OR 

Download this python file as is, make the the necessary changes in notepad, and turn it into an exe to run it directly without installing python.
But you will need to install chromedriver, and make the necessary change to direct the program to look for "chromedriver.exe", or add chromedriver to your path and get rid of the ```chrome_driver = "C:\\change\\path\\to\\chromedriver.exe"``` 

**To install Selenium** <br />
> ```pip install selenium```

**Chrome Driver** <br />
Selenium and Python work together to create a program that can access and interact with the chrome browser. <br />
But to do that, a driver is needed, and that is the Chrome Driver. <br /> 
You must have this to run this program, and the link for it is [here](http://jonathansoma.com/lede/foundations-2018/classes/selenium/selenium-windows-install/), as well as the installation instructions. 

**To run the program** <br />
If you have python installed, you can just run the python file and it'll execute once you have made the changes to the program. 
Change the values, (username, password, email, fname, lname) to ones that are applicable to you and the form. 
There are comments in the file so it'll help guide you through it.

**Contributing** <br />
It doesn't fill out the dropdown choices in the google form, so pull requests are definitely welcome and appreciated! 