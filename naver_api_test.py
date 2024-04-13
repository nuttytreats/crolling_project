import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import pyperclip
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import openpyxl

# 네이버 쇼핑 검색 함수
def search_naver(keyword):
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
    

    return output_text

item = input("검색어를 입력하세요 : ")


result = search_naver(item)
print(result)

