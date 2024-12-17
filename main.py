from dotenv import load_dotenv
import os
import argparse
from naver_login import NaverLogin
from metacode_cafe_attendance import CafeAttendance

def main():
    # 환경변수 로드
    load_dotenv()
    
    # 명령행 인자 파싱
    parser = argparse.ArgumentParser(description='네이버 카페 자동 출석체크 프로그램')
    parser.add_argument('--message', '-m', 
                      default="출석체크",
                      help='출석체크 메시지 (기본값: "출석체크")')
    
    args = parser.parse_args()
    
    # 환경변수에서 로그인 정보 가져오기
    naver_id = os.getenv('NAVER_ID')
    naver_pw = os.getenv('NAVER_PW')

    if not naver_id or not naver_pw:
        raise ValueError("환경 변수에 NAVER_ID와 NAVER_PW가 설정되어 있지 않습니다.")
    
    # 로그인 인스턴스 생성
    naver = NaverLogin()
    
    try:
        # 로그인
        if naver.login(naver_id, naver_pw):
            # 출석체크 인스턴스 생성
            attendance = CafeAttendance(naver.get_driver())
            
            # 출석체크 실행
            if attendance.check_attendance(args.message):
                print("출석체크가 완료되었습니다.")
            else:
                print("출석체크 실패")
                
            # 창 정리
            attendance.cleanup()
        else:
            print("로그인 실패")
            
    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {str(e)}")
        
    finally:
        naver.quit()

if __name__ == "__main__":
    main()
