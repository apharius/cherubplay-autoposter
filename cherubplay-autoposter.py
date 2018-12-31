from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display
from time import sleep
from selenium.webdriver.common.keys import Keys
def main():
    username = input('Username: ')
    password = input('Password: ')
    display = Display(visible=1,size=(1366,768))
    display.start()

    browser = webdriver.Chrome('/usr/bin/chromedriver')
    browser.get('https://cherubplay.co.uk')
    username_field = browser.find_element_by_xpath('//form[@action="/log-in/"]/p/input[@name="username"]')
    password_field = browser.find_element_by_xpath('//form[@action="/log-in/"]/p/input[@name="password"]')
    login_button = browser.find_element_by_xpath('//form[@action="/log-in/"]/p/button')

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    sleep(2) 
    prompt_button = browser.find_element_by_xpath('//button[@class="prompt_button"]')
    prompt_button.click()
    
    prompt_list = browser.find_elements_by_xpath('//select[@id="prompt_id"]/option')   
    for i in range(len(prompt_list)):
        
        select = Select(browser.find_element_by_id('prompt_id'))
        select.select_by_index(i)
        post_button = browser.find_element_by_id('post_button')
        post_button.click()
        sleep(1)
        home_link = browser.find_element_by_id('nav_home')
        home_link.send_keys(Keys.LEFT_CONTROL + Keys.ENTER)
        sleep(1)
        browser.switch_to.window(browser.window_handles[i+1])
    
    print("All prompts posted. To terminate the program and take them down, press Enter.")    
    input()

    display.stop()

if __name__ == "__main__":main()
