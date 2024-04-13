import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pyperclip  # pyperclip 모듈 import

# 네이버 쇼핑 검색 함수
def search_naver(event=None):
    keyword = entry_keyword.get()
    
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(f'https://search.shopping.naver.com/search/all?query={keyword}')
    time.sleep(2)
    browser.refresh()
    time.sleep(2)

    elements = browser.find_elements(By.CLASS_NAME, 'adProduct_depth__s_IUT')
    
    texts = []
    for element in elements:
        sub_elements = element.find_elements(By.CLASS_NAME, 'adProduct_category__ZIAfP.adProduct_nohover__zHCEV')
        for sub_element in sub_elements:
            texts.append(sub_element.text)

    unique_texts = list(set(texts))
    output_text = ">".join(unique_texts)

    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, output_text)
    text_result.config(state=tk.DISABLED)

# 클립보드에 텍스트 복사 함수
def copy_to_clipboard():
    result_text = text_result.get(1.0, tk.END)  # 결과 텍스트 박스의 내용 가져오기
    pyperclip.copy(result_text)  # 클립보드에 복사
    print("Text copied to clipboard.")

root = tk.Tk()
root.title("네이버 쇼핑 검색")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

entry_keyword = ttk.Entry(root, width=50)
entry_keyword.grid(row=0, column=0, padx=10, pady=10)
entry_keyword.bind('<Return>', search_naver)

button_search = ttk.Button(root, text="검색", command=search_naver)
button_search.grid(row=0, column=1, padx=10, pady=10)

text_result = tk.Text(root, height=20, width=100, font=("Helvetica", 20))
text_result.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
text_result.config(state=tk.DISABLED)

# 복사 버튼 추가
button_copy = ttk.Button(root, text="복사", command=copy_to_clipboard)
button_copy.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
