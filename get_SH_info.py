from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_SH_info(url, className, tag_name):
    browser = webdriver.Chrome(r"C:\Users\CHEN WEI XIANG\Downloads\chromedriver_win32\chromedriver.exe")
    browser.get(url)
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, className)))
    data = browser.page_source
    soup = BeautifulSoup(data, 'lxml')
    notice = soup.find('div', class_=className).find_all(tag_name)
    list = []
    for i in notice:
        content = i.text.strip()
        list.append(content.replace('\t', ''))
    browser.quit()
    for x in list:
        print(x)
    print(len(list))
    return list


# get_SH_info(r'http://www.sse.com.cn/disclosure/listedinfo/announcement/', 'sse_list_1', 'em')


