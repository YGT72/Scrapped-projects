from selenium import webdriver
import time
web = webdriver.Chrome()
web.get('https://bloxflip.com/crash')
time.sleep(2)#Sleeps (pause)
ignore = web.find_element_by_xpath('//*[@id="onesignal-slidedown-cancel-button"]')#Grabs path
ignore.click()

inputty = web.find_element_by_xpath('//*[@id="root"]/div/main/header/div[1]/div/button')
inputty.click()

login = web.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[2]/div/div/div/input')
Cookie = ('COOKIE HERE')
#Roblox cookie 
login.send_keys(Cookie)
#loads cookie in

submit = web.find_element_by_xpath('/html/body/div[4]/div[3]/div/div[2]/div/button')
submit.click()
print ('how much you want to risk?:')
z = input() 
print('Ok risking, ' + z)
checker = web.find_element_by_xpath('//*[@id="root"]/div/main/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div')
checker.send_keys(z)
time.sleep(4)
place_bet = web.find_element_by_xpath('//*[@id="root"]/div/main/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/button[9]')
place_bet.click()
