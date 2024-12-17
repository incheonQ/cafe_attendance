from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CafeAttendance:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.main_window = None
        
    def check_attendance(self, message="출석체크"):
        try:
            # 카페로 이동
            self.driver.get("https://cafe.naver.com/love3339")
            self.main_window = self.driver.current_window_handle
            
            # 출석체크 메뉴로 이동
            attendance_menu = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="menuLink10"]'))
            )
            attendance_menu.click()
            
            # iframe 전환
            iframe = self.wait.until(
                EC.presence_of_element_located((By.ID, "cafe_main"))
            )
            self.driver.switch_to.frame(iframe)
            
            # 출석체크 입력
            content_box = self.wait.until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]'))
            )
            content_box.clear()
            content_box.send_keys(message)
            
            # 등록 버튼 클릭
            submit_button = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, '//*[@id="main-area"]/div[3]/div[1]/form/fieldset/div/button'
                ))
            )
            submit_button.click()
            
            time.sleep(2)
            return True
            
        except Exception as e:
            print(f"출석체크 중 오류 발생: {str(e)}")
            return False
        
    def cleanup(self):
        if len(self.driver.window_handles) > 1:
            self.driver.close()
            self.driver.switch_to.window(self.main_window)
