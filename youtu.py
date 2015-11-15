from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("https://boards.4chan.org/mu/")
elem = driver.find_elements_by_class_name("subject")
for i in elem:
    print(i.text)



