from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import pyperclip
import time
import os
import argparse

def naver_cafe_attendance(message="출석체크"):
    # .env 파일 로드
    load_dotenv()
    
    # 환경변수에서 로그인 정보 가져오기
    naver_id = os.getenv('NAVER_ID')
    naver_pw = os.getenv('NAVER_PW')

    if not naver_id or not naver_pw:
        raise ValueError("환경 변수에 NAVER_ID와 NAVER_PW가 설정되어 있지 않습니다.")

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    main_window = None
    
    try:
        # 네이버 로그인 페이지로 이동
        driver.get("https://nid.naver.com/nidlogin.login")
        time.sleep(1)
        
        # ID 입력
        id_input = wait.until(EC.presence_of_element_located((By.ID, 'id')))
        pyperclip.copy(naver_id)
        id_input.click()
        id_input.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)
        
        # 비밀번호 입력
        pw_input = driver.find_element(By.ID, 'pw')
        pyperclip.copy(naver_pw)
        pw_input.click()
        pw_input.send_keys(Keys.CONTROL, 'v')
        time.sleep(1)
        
        # 로그인 버튼 클릭
        login_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        )
        login_button.click()
        time.sleep(2)
        
        # 카페로 이동
        driver.get("https://cafe.naver.com/love3339")
        main_window = driver.current_window_handle
        
        # 출석체크 메뉴로 이동
        attendance_menu = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menuLink10"]'))
        )
        attendance_menu.click()
        
        # iframe 전환
        iframe = wait.until(
            EC.presence_of_element_located((By.ID, "cafe_main"))
        )
        driver.switch_to.frame(iframe)
        
        # 출석체크 입력
        content_box = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="contents"]'))
        )
        content_box.clear()
        content_box.send_keys(message)
        
        # 등록 버튼 클릭
        submit_button = wait.until(
            EC.element_to_be_clickable((
                By.XPATH, '//*[@id="main-area"]/div[3]/div[1]/form/fieldset/div/button'
            ))
        )
        submit_button.click()
        
        time.sleep(2)
        print("출석체크가 완료되었습니다.")
        
        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(main_window)
            
    except Exception as e:
        print(f"오류 발생: {str(e)}")
        
    finally:
        driver.quit()

def main():
    parser = argparse.ArgumentParser(description='네이버 카페 자동 출석체크 프로그램')
    parser.add_argument('--message', '-m', 
                      default="출석체크",
                      help='출석체크 메시지 (기본값: "출석체크")')
    
    args = parser.parse_args()
    naver_cafe_attendance(args.message)

if __name__ == "__main__":
    main()
