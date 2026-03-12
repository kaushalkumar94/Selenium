from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://selenium.dev")

print("Page Title:", driver.title)

input("Press Enter to close browser...")

driver.quit()