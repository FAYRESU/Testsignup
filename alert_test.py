import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

class GoogleTest(unittest.TestCase):
    
    def setUp(self):
        s = Service(r"D:\chromedriver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://sc.npru.ac.th/sc_shortcourses/signup")
    
    def test_fill_form(self):
        driver = self.driver


        name_title = Select(driver.find_element(By.ID, "nameTitleTha"))
        name_title.select_by_value("นางสาว") 

       
        driver.find_element(By.ID, "firstnameTha").send_keys("ณัฐกานต์")
        driver.find_element(By.ID, "lastnameTha").send_keys("จำรัสภูมิ")

        
        name_title_eng = Select(driver.find_element(By.ID, "nameTitleEng"))
        name_title_eng.select_by_value("Ms.")

        
        driver.find_element(By.ID, "firstnameEng").send_keys("Natthakan")
        driver.find_element(By.ID, "lastnameEng").send_keys("Jamratphum")

       
        Select(driver.find_element(By.ID, "birthDate")).select_by_value("26")
        Select(driver.find_element(By.ID, "birthMonth")).select_by_value("12")
        Select(driver.find_element(By.ID, "birthYear")).select_by_value("2004")

        
        driver.find_element(By.ID, "idCard").send_keys("1429900541531")
        driver.find_element(By.ID, "password").send_keys("Natthakan678")
        driver.find_element(By.ID, "mobile").send_keys("0821505710")
        driver.find_element(By.ID, "email").send_keys("natthaan57101@gmail.com")
        driver.find_element(By.ID, "address").send_keys("หอพักศรีพยุงเฮ้าส์")

       
        Select(driver.find_element(By.ID, "province")).select_by_value("นครปฐม")

       
        driver.find_element(By.ID, "district").send_keys("เมือง")
        driver.find_element(By.ID, "subDistrict").send_keys("วังตะกู")
        driver.find_element(By.ID, "postalCode").send_keys("73000")

       
        accept_checkbox = driver.find_element(By.XPATH, "//*[@id='accept']")
        if not accept_checkbox.is_selected():
            driver.execute_script("arguments[0].click();", accept_checkbox)

        
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
