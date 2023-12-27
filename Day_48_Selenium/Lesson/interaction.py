from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#Find the number of articles on wikipedia.org
#driver.get("https://en.wikipedia.org")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(f"The number of English Articles is {article_count.text}")

#Click on the article_count link
#article_count.click()

# content_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portals.click()

#Type in something in the search bar, and then the enter key
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# #search.send_keys(Keys.ENTER)
# search.submit()


#CHALLENGE - Fill out form on http://secure-retreat-92358.herokuapp.com/
driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("Joe")
lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("Smith")
email = driver.find_element(By.NAME, value="email")
email.send_keys("joe@joesmith.org")
button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()


#driver.quit()