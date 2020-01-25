import selenium
import time
from selenium import webdriver
import codecs

def wait_secs(sec = 1):
	for i in range(sec):
		time.sleep(1)
		print(i+1)
	

#Open Browser
driver = webdriver.Chrome()

#open Costumers page
driver.get("http://geektyper.com/nasa/")

elem = driver.find_element_by_xpath('//*[@id="console"]                                          ')

wait_secs(10)

while 1:
	 elem.send_keys("uishrflqhrfçehrsligeç")
