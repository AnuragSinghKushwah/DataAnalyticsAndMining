from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://github.com/login")
id = "vicky786rajawat@gmail.com"
passwrd = "thakur786"

driver.find_element_by_id("login_field").send_keys(id)
driver.find_element_by_id("password").send_keys(passwrd)
driver.find_element_by_name("commit").click()