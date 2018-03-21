'''
Pokemon Web Crawler
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

import pprint as pp
#colocar o chromedriver.exe no mesmo diretorio do python
#browser = webdriver.Chrome(executable_path=r"chromedriver.exe")
#browser.get('http://www.serebii.net/')

def make_waitfor_elem_updated_predicate(driver, waitfor_elem_xpath):
    elem = driver.find_element_by_xpath(waitfor_elem_xpath)

    def elem_updated(driver):
        try:
            elem.text
        except StaleElementReferenceException:
            return True
        except:
            pass

        return False

    return lambda driver: elem_updated(driver)

class Pokemon:
    def __init__(self,driver):
        self.driver = driver
        self.url = 'http://www.serebii.net/'

    def navigate(self):
        import time
        self.driver.get(self.url)
        self.driver.implicitly_wait(2)


    def scrape(self):
        self.navigate()
        self.driver.find_element_by_xpath('//*[@id="menu"]/a[9]').click()
        currentURL = driver.getCurrentUrl();
        menu = Select(self.driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[2]/font/div[3]/table/tbody/tr[1]/td[1]/form/select'))
        self.driver.implicitly_wait(3) # seconds
        #self.driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[2]/font/div[3]/table/tbody/tr[1]/td[1]/form/select/option[1]').click()


        option = menu.select_by_index(1)

        #pp.pprint(temp.text)


browser = webdriver.Chrome(executable_path=r"chromedriver.exe")

p = Pokemon(browser)
p.navigate()
p.scrape()

#browser.quit()
