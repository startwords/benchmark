

# import selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# import keys for text entry
from selenium.webdriver.common.keys import Keys
# import time module
import time

# attempt to fix bug july 16
caps = DesiredCapabilities.FIREFOX
caps["marionette"] = True
caps["binary"] = "/usr/bin/firefox"
driver = webdriver.Firefox(capabilities=caps)


# define webdriver as firefox
#browser = webdriver.Firefox()

# start the timer for page call
start_pagecall = time.time()
# get the page
driver.get('https://library.wrdsb.ca/library/Discovery/Home.aspx')
# end the timer for page call
end_pagecall = time.time()
# display the elapsed time for page call
elapsed_pagecall = end_pagecall - start_pagecall
print
print("Page call elapsed time in seconds is:")
print(elapsed_pagecall)

# start the timer for search
start_search = time.time()
# find the text box and define it as input area
input = driver.find_element_by_id('searchTxt-inputEl')
# send a search term
input.send_keys('science')
# find the search button
input2 = driver.find_element_by_id('btnSearchSubmit')
# click the search button
input2.send_keys(Keys.RETURN)

# need a confirmation that page is loaded! Current output may be inaccurate due to vagaries of js

# end the clock
end_search = time.time()
# calculate and print elapsed time
elapsed_search = end_search - start_search
print
print("Search elapsed time in seconds is:")
print(elapsed_search)
print

# close the browser window
driver.quit()
