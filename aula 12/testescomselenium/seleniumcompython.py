from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.nuancesrequinte.com")

print(driver.current_url)
print(driver.capabilities["browserVersion"])
element = driver.find_element(by=id,h-b-t)
element.click()


driver.close()

