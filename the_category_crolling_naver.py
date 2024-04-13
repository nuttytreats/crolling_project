import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 네이버 쇼핑 검색 함수
def search_naver(event=None):  # 엔터 키를 처리하기 위해 event 매개변수 추가
    keyword = entry_keyword.get()
    
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(f'https://search.shopping.naver.com/search/all?query={keyword}')
    time.sleep(2)  # 페이지가 로드되고 동적으로 요소가 로드될 시간을 줍니다.
    browser.refresh()
    time.sleep(2)

    # 모든 adProduct_depth__s_IUT 클래스를 가진 요소 가져오기
    elements = browser.find_elements(By.CLASS_NAME, 'adProduct_depth__s_IUT')
    
    # 각 요소에 포함된 adProduct_category__ZIAfP adProduct_nohover__zHCEV 클래스를 가진 요소의 텍스트 가져오기
    texts = []
    for element in elements:
        sub_elements = element.find_elements(By.CLASS_NAME, 'adProduct_category__ZIAfP.adProduct_nohover__zHCEV')
        for sub_element in sub_elements:
            texts.append(sub_element.text)

    # 중복된 단어를 제거하기 위해 집합(set)으로 변환 후 리스트로 다시 변환
    unique_texts = list(set(texts))
    # 가져온 텍스트 출력
    output_text = ">".join(unique_texts)

    # 가져온 텍스트 출력
    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, output_text)
    text_result.config(state=tk.DISABLED)

# tkinter 창 생성
root = tk.Tk()
root.title("네이버 쇼핑 검색")

# 전체 화면 크기로 설정
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# 검색어 입력 텍스트 상자 생성
entry_keyword = ttk.Entry(root, width=50)  # 너비를 더 크게 조정
entry_keyword.grid(row=0, column=0, padx=10, pady=10)
entry_keyword.bind('<Return>', search_naver)  # 엔터 키에 대한 이벤트 바인딩

# 검색 버튼 생성
button_search = ttk.Button(root, text="검색", command=search_naver)
button_search.grid(row=0, column=1, padx=10, pady=10)

# 결과 출력 텍스트 박스 생성
text_result = tk.Text(root, height=20, width=100, font=("Helvetica", 20))  # 폰트 크기 조정
text_result.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
text_result.config(state=tk.DISABLED)  # 텍스트 박스를 읽기 전용으로 설정

root.mainloop()