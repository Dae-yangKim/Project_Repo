# import libraires

import concurrent.futures
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import time
import missingno as msno
from bs4 import BeautifulSoup

# ====================================================================================================================
# 함수 정의

# 책의 URL에 따라서 평점을 가져오는 코드이다.

def get_score(url):
    res = requests.post(url)
    soup = BeautifulSoup(res.text , 'html5lib')
    tag_name = "#yesSchList > li > div > div.item_info > div.info_row.info_rating > span.rating_grade > em"
    score = soup.select(tag_name)
    try:
        return score[0].text
    except:
        return np.NaN
        
# 책의 판매지수 가져오는 코드이다.

def get_sale(url):
    res = requests.post(url)
    soup = BeautifulSoup(res.text , 'html5lib')
    tag_name = "#yesSchList > li > div > div.item_info > div.info_row.info_rating > span.saleNum"
    sale = soup.select(tag_name)
    try:
        return sale[0].text
    except:
        return np.NaN

# 병렬작업 함수 구현

def scrape_scores_parallel(books_url):
    book_scores = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        scores = list(executor.map(get_score , books_url))
    
    for i , url in enumerate(books_url):
        book_scores[url.split('=')[2]] = scores[i]
    
    return book_scores

def scrape_sales_parallel(books_url):
    book_sales = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        sales = list(executor.map(get_sale , books_url))

    for i , url in enumerate(books_url):
        book_sales[url.split('=')[2]] = sales[i]
    
    return book_sales

# ====================================================================================================================

if __name__ == "__main__":

    # 책의 URL을 가져오는 코드
    books_url = [] # URL을 기록
    book_data = pd.read_excel("Data_01.xlsx")# 책의 URL 저장

    URL = input().rstrip()
    for isbn in book_data['ISBN13번호'].sort_values(ascending=False).unique():
        books_url.append(f"{URL}{isbn}")

    # timestamp
    start = time.time()

    # 평점 스크래핑
    print("---------- 병렬 스크랩핑 중 ----------")
    book_scores_parallel = scrape_scores_parallel(books_url)
    print("---------- 평점 스크래핑 완료 ----------")
    print(book_scores_parallel)

    end = time.time()

    # 걸린 시간
    print(f"Time Stamp : {end - start}")

    # timestamp
    start = time.time()

    # 평점 스크래핑
    print("---------- 병렬 스크랩핑 중 ----------")
    book_sales_parallel = scrape_sales_parallel(books_url)
    print("---------- 판매지수 스크래핑 완료 ----------")
    print(book_sales_parallel)

    end = time.time()

    # 걸린 시간
    print(f"Time Stamp : {end - start}")

    # 데이터프레임으로 만든 뒤에 , 저장
    data = pd.DataFrame(
        {
            'ISBN' : book_scores_parallel.keys() ,
            'Score' : book_scores_parallel.values()
        }
    )

    data = pd.DataFrame(
        {
            'ISBN' : book_sales_parallel.keys() ,
            'Sale' : book_sales_parallel.values()
        }
    )

    # 데이터 저장
    data.to_csv('Score.csv' , index = False)
    data.to_csv('Sale.csv' , index = False)

    # 데이터 합병
    sale = pd.read_csv('Sale.csv')
    score = pd.read_csv('Score.csv')
    merged_data = pd.merge(sale , score , on = 'ISBN' , how = 'outer')

    # 합병 데이터 csv파일 저장
    merged_data.to_csv('Merged_Data.csv' , index = False)