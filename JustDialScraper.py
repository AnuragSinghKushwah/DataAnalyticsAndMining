from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.justdial.com/Bhopal/Restaurants")
# print(driver.page_source)
for div in driver.find_elements_by_class_name("cntanr"):
    print("*****************************************")
    print(div.click())

