from selenium import webdriver
from bs4 import BeautifulSoup

def extract_keywords(url):
    # ChromeDriver 경로 설정 (본인 컴퓨터에 맞게 수정)
    driver_path = '/path/to/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 브라우저를 표시하지 않고 백그라운드에서 실행
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # 클래스가 'adProduct_depth__s_IUT'인 요소를 찾아 텍스트 추출
    keywords = soup.find_all(class_='adProduct_depth__s_IUT')
    
    # 추출한 키워드 출력
    for keyword in keywords:
        print(keyword.text.strip())
    
    driver.quit()

# 네이버 쇼핑 페이지 URL 설정
url = 'https://shopping.naver.com/'

# 키워드 추출 함수 호출
extract_keywords(url)
