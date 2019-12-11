import requests
from selenium import webdriver


IS_LINUX = False

chrome = webdriver.Chrome(executable_path="/Users/jerem/Downloads/chromedriver" if not IS_LINUX else "./chromedriver_linux")

chrome.get("https://www.amazon.fr")
pass_verif = chrome.find_element_by_link_text("Essayez une autre image")
pass_verif.click()

link = chrome.find_element_by_link_text("Voir tout")
link.click()

all_widgets = chrome.find_elements_by_id("widgetContent")

first_line = all_widgets[0]
all_first_line_elements = first_line.find_elements_by_class_name('a-section')


_ = [print(elt.text+ "\n")  for elt in all_first_line_elements]