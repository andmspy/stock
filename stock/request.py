import requests
import fake_useragent
import time
from bs4 import BeautifulSoup
from selenium import webdriver



class news:

    def __init__(self):
        pass


    def chrome_options(cls):
        mobile_emulation = {"deviceMetrics": {"width": 375, "height": 667, "pixelRatio": 2.0},
                            "userAgent": "Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        return chrome_options


    def user_agent(self):
        user_agent = fake_useragent.UserAgent()
        return user_agent.random


    def get_website(self):
        website_list = []
        with open('website.txt', 'r', encoding='utf-8') as f:
            for i in f:
                if i.startswith('h'):
                    website_list.append(i)
        return website_list

    def requests(self):
        website = r'http://www.gov.cn/xinwen/yaowen/headlines.htm'
        headers = {'user-agent': self.user_agent()}
        wb_data = requests.get(website, headers=headers)
        return wb_data.content


    def beautifulsoup(self):
        wb_data = self.requests()
        soup = BeautifulSoup(wb_data, 'lxml')
        content = soup.find('div', class_='list list_1 list_2').findAll('h4')
        for i in content:
            print(i.strip())
            time.sleep(1)


    def selenium(self):
        driver = webdriver.PhantomJS()
        driver.get(r'http://www.gov.cn/xinwen/yaowen/headlines.htm')
        # content = driver.find_element_by_class_name('list list_1 list_2')
        wb_data = driver.page_source
        soup = BeautifulSoup(wb_data, 'lxml')
        content = soup.find('div', class_='list list_1 list_2').findAll('a')
        for i in content:
            print(i['href'], i.text)


if __name__ == '__main__':
    News = news()
    News.selenium()
