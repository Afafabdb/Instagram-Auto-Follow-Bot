from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from random import seed
from random import randint
import pathlib

follow_username = ["instagram", "spacewitchix", "official_pepe"]
username = "USERNAME"
password = "PASSWORD"

def login():
	#Accept cookie popup
	If_element_is_here_do_click("/html/body/div[4]/div/div/button[1]")
	
	#Login
	time.sleep(getRandomTime())
	driver.find_element_by_xpath("//input[@name=\"username\"]")\
		.send_keys(username)
	driver.find_element_by_xpath("//input[@name=\"password\"]")\
		.send_keys(password)
	time.sleep(getRandomTime())      
	driver.find_element_by_xpath('//button[@type="submit"]').click()
	
	#Notifications popup
	If_element_is_here_do_click("/html/body/div[5]/div/div/div/div[3]/button[1]")

def follow():
	for user in follow_username:
		#Go on profile
		driver.get("https://www.instagram.com/" + user)

		#Follow button
		If_element_is_here_do_click("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button")

def If_element_is_here_do_click(xpath_arg):
		executed = 0
		while (executed == 0):
			try:
				driver.find_element(By.XPATH, xpath_arg).click()
				executed = 1
				print("Clicked")
			except:
				print("No")
				time.sleep(0.5)

class InstaBot:
	def __init__(self):
		global driver, username, password
	
		driver = webdriver.Chrome(pathlib.Path(__file__).parent.absolute().joinpath("chromedriver"))
		options = webdriver.ChromeOptions()
		options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
		driver = webdriver.Chrome(chrome_options=options)
		driver.get("https://instagram.com")

		login()
		
		follow()

		input('')
		# driver.quit()

def getRandomTime():
        randTime = randint(1, 2)
        return randTime
        
InstaBot()

# https://www.programcreek.com/python/example/93851/selenium.webdriver.common.by.By.XPATH
# https://stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python