from selenium import webdriver
from selenium.webdriver.common.by import By 

#Selenium Docs - https://selenium-python.readthedocs.io/
#XPath Tutorial - https://www.w3schools.com/xml/xpath_intro.asp


#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
#Get the price of an Instant Pot Duo 9in1 from Amazon
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_1?crid=2LV2B3AHCARUO&keywords=instant+pot+duo+plus+9-in-1&qid=1696137224&sprefix=instantpot+duo+plus%2Caps%2C101&sr=8-1")

#Use the find_element function to search by Class - the price uses a class of "a-price-whole" for the dollar part
#and a class of "a-price-fraction" for the cents (they have a separate class element for the dollar sign and the decimal too)
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is ${price_dollar.text}.{price_cents.text}")

#Look at the search bar element on python.org using By.NAME
#<input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">
driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

#Look at the Go button on python.org using By.ID
#<button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">GO</button>
# go_button = driver.find_element(By.ID, value="submit")
# print(go_button.tag_name)
# print(go_button.size)

#Look at the links to the docs on python.org using By.CSS_SELECTOR
#content > div > section > div:nth-child(1) > div.small-widget.documentation-widget > p:nth-child(3) > a
# docs_link = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget p a")
# print(docs_link.text)

#Look at the "Submit Website Bugs" Link
#//*[@id="site-map"]/div[2]/div/ul/li[3]/a
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

#Look at the Upcoming Events List Element find all list items and create a dictionary of event dates and names
##content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child(1)
upcoming_events_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget div ul li time")
upcoming_events_links = driver.find_elements(By.CSS_SELECTOR, value=".event-widget div ul li a")

events = {}
for i in range(len(upcoming_events_dates)):
    events[i] = {"time": upcoming_events_dates[i].text, "name": upcoming_events_links[i].text}
print(events)

#Close the active tab
#driver.close()

#Quit the browser
driver.quit()