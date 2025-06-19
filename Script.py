from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com")
driver.maximize_window()

actual_title = "Swag Labs"
title1 = driver.title
print("Page Title", title1)

assert actual_title== title1, "Title dose not match then page does not load correcrlt"

#login

username =driver.find_element(By.ID, "user-name")
password =driver.find_element(By.ID, "password")
login_button= driver.find_element(By.ID, "login-button")


username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()
assert "saucedemo.com" in driver.current_url, "Login failed"
print("login pass")

#logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
logout_link =driver.find_element(By.ID, "logout_sidebar_link")
logout_link.click()


# assert "saucedemo.com" in driver.current_url, "logout fail"
# print("login pass")

#invalid login
username =driver.find_element(By.ID, "user-name")
password =driver.find_element(By.ID, "password")
login_button= driver.find_element(By.ID, "login-button")

username.send_keys("user")
password.send_keys("sauce")
login_button.click()
error_msg = driver.find_element(By.XPATH, "//h3[contains(@data-test, 'error')]")
assert error_msg.is_displayed()
print("massage display")

#Re-login

driver.find_element(By.ID, "user-name").clear()
username.send_keys("standard_user")
driver.find_element(By.ID, "password").clear()
password.send_keys("secret_sauce")
login_button.click()


#add to card

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()

#count

cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
assert cart.text == "4", "Cart item not match"
print("4 item added")


#shoppint continue

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
driver.find_element(By.ID, "continue-shopping").click()
assert "inventory" in driver.current_url, "shopping not return continue"
print("shopping done")

#Checkout Process
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
driver.find_element(By.ID, "checkout").click()


#Cust. Details
driver.find_element(By.ID, "first-name").send_keys("Rakesh")
driver.find_element(By.ID, "last-name").send_keys("Katre")
driver.find_element(By.ID, "postal-code").send_keys("441670")
driver.find_element(By.ID, "continue").click()

#price verification
total_price =driver.find_element(By.CLASS_NAME, "summary_total_label")
assert total_price.is_displayed(), "Price not display"
print("Price display")
driver.find_element(By.ID, "finish").click()

#a confirmation message


#back to home
driver.find_element(By.ID, "back-to-products").click()
assert "invent" in driver.current_url, "not return page"
print("return page")

#logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
driver.find_element(By.ID, "logout_sidebar_link").click()



login_button= driver.find_element(By.ID, "login-button")
assert login_button.is_displayed(), "Logout fail"
print("log-out successfully")

driver.quit()
















