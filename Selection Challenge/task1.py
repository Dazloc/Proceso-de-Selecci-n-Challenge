# UI Automated test using Selenium WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random

#A function to fill forms is created to use when creating a user and the shipping info
def fill(a,b):
    nombre = driver.find_element(By.NAME, value=a)
    nombre.click()
    nombre.send_keys(b)
    
#You initiate the driver and go to the website
driver = webdriver.Chrome()
driver.get("https://demo.evershop.io/")

#You go to the login page and choose to create an account
buttons = driver.find_elements(By.TAG_NAME, 'a')
for button in buttons:
    if button.get_attribute('href') =="https://demo.evershop.io/account/login":
        button.click()
        break
driver.find_element(By.LINK_TEXT, "Create an account").click()

#Information for the user to be created, a random number is added to the email since you cant repeat emails and this will need to run several times
rand= str(random.randint(1000,1999))
account_info = ['Pablo','pabloo'+rand+'@mail.com','12345']

#The function is used to fill the form and create the new user
fill("full_name",account_info[0])
fill("email",account_info[1])
fill("password",account_info[2])
submit = driver.find_element(By.CLASS_NAME,value="form-submit-button")
submit.click()

#We navegate to the Men section for our first item
link = driver.find_element(By.LINK_TEXT,value="Men")
link.click()
first = driver.find_element(By.CLASS_NAME,value="listing-tem")
first.click()
size=driver.find_element(By.LINK_TEXT,value="S")
size.click()
color=driver.find_element(By.LINK_TEXT,value="Black")
color.click()
time.sleep(1)
cart=driver.find_element(By.CLASS_NAME,value="mt-1")
cart.click()

#We get our second item from the Women section
link = driver.find_element(By.LINK_TEXT,value="Women")
link.click()
first = driver.find_element(By.CLASS_NAME,value="listing-tem")
first.click()
size=driver.find_element(By.LINK_TEXT,value="S")
size.click()
color=driver.find_element(By.LINK_TEXT,value="Brown")
color.click()
time.sleep(1)
cart=driver.find_element(By.CLASS_NAME,value="mt-1")
cart.click()

#We get our third and last item from the Kids section
link = driver.find_element(By.LINK_TEXT,value="Kids")
link.click()
first = driver.find_element(By.CLASS_NAME,value="listing-tem")
first.click()
size=driver.find_element(By.LINK_TEXT,value="S")
size.click()
color=driver.find_element(By.LINK_TEXT,value="Black")
color.click()
time.sleep(1)
cart=driver.find_element(By.CLASS_NAME,value="mt-1")
cart.click()

#After getting our items, we go to the cart to check out
home=driver.find_element(By.CLASS_NAME,value="logo-icon")
home.click()
gotocart=driver.find_element(By.CLASS_NAME,value="mini-cart-icon")
gotocart.click()
checkout = driver.find_element(By.XPATH, "//span[contains(text(), 'CHECKOUT')]")
checkout.click();

#This is the shipping information we'll use
shipping_info = ['Pablo','987654321','Main St 125','Lima','China','Guangxi','15098']
fill("address[full_name]",shipping_info[0])
fill("address[telephone]",shipping_info[1])
fill("address[address_1]",shipping_info[2])
fill("address[city]",shipping_info[3])
country_dropdown = driver.find_element(By.NAME, value="address[country]")
drop=Select(country_dropdown)
drop.select_by_visible_text(shipping_info[4])
prov_dropdown = driver.find_element(By.NAME, value="address[province]")
drop=Select(prov_dropdown)
drop.select_by_visible_text(shipping_info[5])
fill("address[postcode]",shipping_info[6])
time.sleep(2)

#We pick our shipping price
shipping_method = driver.find_element(By.CLASS_NAME, value="radio-unchecked")
shipping_method.click()
checkout = driver.find_element(By.XPATH, "//span[contains(text(), 'Continue to payment')]")
checkout.click();
time.sleep(1)

#We pick our method of payment
payment = driver.find_element(By.XPATH, "//div[@class='py-2']/div/div/div/a")
payment.click()
place = driver.find_element(By.XPATH, "//span[contains(text(), 'Place Order')]")
place.click()
time.sleep(2)

#We verify our shipping and account information is shown in the "Order placed" screen
order=driver.find_element(By.CLASS_NAME, value="grid")
for x in shipping_info:
    if x in order.text:
        print(f"The element contains {x}.")
    else:
        print(f"The element does not contain the search text: {x}.")
for x in account_info:
    if x in order.text:
        print(f"The element contains {x}.")
    else:
        print(f"The element does not contain the search text: {x}.")

driver.quit()