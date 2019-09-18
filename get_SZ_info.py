from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


url = r'http://www.szse.cn/disclosure/listed/notice/'


def parse(data):
    soup = BeautifulSoup(data, 'lxml')
    notice = soup.find('div', class_='table-con-outer').find_all('td')
    list_all = []
    for i in range(0, len(notice), 4):
        code = notice[i].text.replace('\n', '')
        name = notice[i+1].text.replace('\n', '')
        title = notice[i+2].text.replace('\n', '')
        date = notice[i+3].text.replace('\n', '')
        list_signle = [code.replace('\t', ''), name.replace('\t', ''), title.replace('\t', ''), date.replace('\t', '')]
        list_all.append(list_signle)
    for x in list_all:
        print(x)
    print(len(list_all))
    red_notice = soup.find('div', class_='noticetip')
    print(red_notice.text)


def get_page_info():
    option = Options()
    option.add_argument(argument='--headless')
    option.add_argument('--disable-gpu')
    browser = webdriver.Chrome(r"C:\Users\CHEN WEI XIANG\Downloads\chromedriver_win32\chromedriver.exe", options=option)
    browser.get(url)
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'paginator')))
    page = '#paginator > li.next > a'
    while True:
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'table-con-outer')))
        data = browser.page_source
        parse(data)
        browser.find_element_by_css_selector(page).click()
        time.sleep(10)


get_page_info()