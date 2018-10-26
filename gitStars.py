from selenium import webdriver
import time
browser = webdriver.Firefox()

browser.get("https://www.github.com")
string = "loremIpsum91"
i = 1
num = input("Enter the number of stars you'd like: ")
for i in range(num):
    browser.find_element_by_id("user[login]").send_keys(string + str(i))
    browser.find_element_by_id("user[email]").send_keys(
        string + str(i) + "@gmail.com")
    password_element = browser.find_element_by_id("user[password]")
    password_element.send_keys("qwerty123$")
    password_element.submit()
    time.sleep(2)
    browser.get("<repo-to-be-starred>")
    script = "var button=document.getElementsByTagName('Button')[3].click()"
    browser.execute_script(script)
    script = "var button=document.getElementsByClassName('dropdown-signout')[1].click()"
    browser.execute_script(script)
    time.sleep(2)
