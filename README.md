```markdown
# 네이버 카페 자동 출석체크 프로그램

네이버 카페의 출석체크를 자동화하는 파이썬 프로그램입니다.

## 🔨 기능 🔨

- 네이버 자동 로그인
- 지정된 카페 접속
- 출석체크 게시판 자동 이동
- 사용자 지정 메시지로 출석체크

## 👷 설치 방법 👷

1. 저장소 클론
```
git clone [repository-url]
cd naver-cafe-attendance
```

2. 필요한 패키지 설치
```
pip install -r requirements.txt
```

## ⚙️ 환경 설정 ⚙️

1. `.env` 파일 생성 후 아래 내용 추가:
```
NAVER_ID=your_naver_id
NAVER_PW=your_naver_password
```

2. 본인 Chrome 버전에 맞는 Chrome Web Driver 다운로드 후 폴더에 추가
https://googlechromelabs.github.io/chrome-for-testing/

## 사용 방법

1. 기본 출석체크
```
python main.py
```

2. 사용자 지정 메시지로 출석체크
```
python main.py -m "출석체크! 오늘도 화이팅!"
# 또는
python main.py --message "출석체크! 오늘도 화이팅!"
```

## 📁 프로젝트 구조 📁

```
cafe-attendance/
├── main.py           # 메인 실행 파일
├── naver_login.py    # 네이버 로그인 모듈
├── attendance.py     # 출석체크 모듈
├── requirements.txt  # 의존성 패키지 목록
├── .env              # 환경 변수 파일
├── chromedriver.exe  # 크롬 웹 드라이버
└── README.md         # 프로젝트 설명서
```

## ⚠️ 주의사항 ⚠️

- Chrome 브라우저가 설치되어 있어야 합니다.
- 네이버의 보안 정책에 따라 로그인 시 추가 인증이 필요할 수 있습니다.
- 과도한 자동화는 계정 제재의 원인이 될 수 있으니 주의하시기 바랍니다.
- 본 프로그램은 메타코드 카페(https://cafe.naver.com/love3339)의 출석체크에 한정된 기능입니다.
```