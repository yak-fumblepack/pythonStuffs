from selenium import webdriver
from selenium.webdriver.support.ui import Select

#Change chrome driver path accordingly
chrome_driver = "C:\\change\\path\\to\\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver)
driver.get("") #this is where you put the applicable form, and change the ending: "formview" to "formResponse"  

#Change values to your values (your student number, your password, your email, your first name, your last name)
email = ''
fname = ''
lname = ''
teachername = ''

#Each driver performs an action
#Each of the words inside the brackets with quotations are names that describe each element in the website, so that selenium can find it and perform the necessary actions

#disclaimer, most of the actions might not be needed because for my use, selenium opens chrome in a guest window
#Each driver performs an action
#Each of the words inside the brackets with quotations are names that describe each element in the website, so that selenium can find it and perform the necessary actions
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input").send_keys(email)#fills out the actual form portion requiring the email
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(username)#fills out the student number
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(fname)#fills out first name
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(lname)#fills out last name
driver.implicitly_wait(5)
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(teachername)#fills out the teacher's name
driver.implicitly_wait(5)

"""the rest will come very soon but i don't necessarily have the time to perfect this yet,
   but it still fills out most of the fields, only the drop down menus are not filled out
   so pull requests are most welcome and appreciated!"""
