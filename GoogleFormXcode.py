from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/SarguneKalsi/Desktop/Python_Projects/chromedriver')

import string
import random
import time

def email_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def apt_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


counter = 0
while counter <= 20:
    counter + 2
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdkJ3vb-oP_t_tWwnBTS1_lWIAmuUsdK4XFd0KjCOD6cB18Cg/viewform?c=0&w=1')
    string = "string"
    email = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input'
    emailEnter = driver.find_element_by_xpath(email)
    emailEnter.send_keys(email_generator()+'@enugrasaio.club')
    emailEnter.submit()

    shoeSizeV1 = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/input'
    shoeSizeEnter = driver.find_element_by_xpath(shoeSizeV1)
    shoeSizeEnter.send_keys('shoe_size')
    shoeSizeEnter.submit()

    #option1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div[2]/div/content/div/label[1]/div/div[1]')
    #option1.click()

    #change the button you want to select by changing the number following label[x]

    option2 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div[2]/div/content/div/label[2]/div/div[1]')
    option2.click()

    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/textarea')
    address.send_keys('123 Main Street Apt '+ apt_generator())



    #time.sleep(3)



    buttonSubmit = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/content/span'
    btnSubmit = driver.find_element_by_xpath(buttonSubmit)
    btnSubmit.click()



#app > div > div:nth-child(1) > div.main___OcwLI > div > div:nth-child(4) > section > div > section.main___37gtD.col-l-12.col-m-6.col-s-12.tilesDtMultiple___36H4l.padded___1pd7D.fadeIn.fadeInActive.color-theme-white___DH74V.content-align-center.text-justify-center___1OY1f.vertical-align-bottom___33rqe.teaser-large > a > div.content___ZWxFr.tileContent___2vSFG.fadeIn___230F_.fadeInActive___3ArVs > div > div > div > button
