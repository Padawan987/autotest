from selenium import webdriver
import unittest
	
chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')


assert 'cb1-element' in chrome_browser.page_source

def button_text():
	button = chrome_browser.find_element_by_class_name('btn-primary')
	button_text = button.get_attribute('value')
	return button_text

def click_button():
	button_text_in = button_text()
	button = chrome_browser.find_element_by_class_name('btn-primary')
	button.click()
	button_text_out = button_text()
#	print(f'Button changed from {button_text_in} new value is {button_text_out}')
	return button_text_out



# ------------ Click on button to check all checkboxes at once
assert 'Uncheck All' in click_button()

checkbox = chrome_browser.find_elements_by_class_name('cb1-element')

assert 'True' in str(any(checkbox))
print('1. Click on button to check all checkboxes at once - CHECKED OK')


# ------------When you check all the checkboxes, button will change to 'Uncheck All'
assert 'Check All' in click_button()

for box in checkbox:
 	box.click()

assert 'Uncheck All' in button_text()

print('2. When you check all the checkboxes, button will change to Uncheck All - CHECKED OK')

# -------When you uncheck at least one checkbox, button will change to 'Check All'
for box in checkbox:
 	box.click()
 	assert 'Check All' in button_text()

print('3. When you uncheck at least one checkbox, button will change to Check All - CHECKED OK')


chrome_browser.close()