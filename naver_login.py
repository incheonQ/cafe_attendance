from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time
import os

class NaverLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        
    def login(self, naver_id, naver_pw):
        try:
            # 네이버 로그인 페이지로 이동
            self.driver.get("https://nid.naver.com/nidlogin.login")
            time.sleep(1)
            
            # ID 입력
            id_input = self.wait.until(EC.presence_of_element_located((By.ID, 'id')))
            pyperclip.copy(naver_id)
            id_input.click()
            id_input.send_keys(Keys.CONTROL, 'v')
            time.sleep(1)
            
            # 비밀번호 입력
            pw_input = self.driver.find_element(By.ID, 'pw')
            pyperclip.copy(naver_pw)
            pw_input.click()
            pw_input.send_keys(Keys.CONTROL, 'v')
            time.sleep(1)
            
            # 로그인 버튼 클릭
            login_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
            )
            login_button.click()
            time.sleep(2)
            
            return True
            
        except Exception as e:
            print(f"로그인 중 오류 발생: {str(e)}")
            return False
    
    def get_driver(self):
        return self.driver
    
    def quit(self):
        self.driver.quit()
