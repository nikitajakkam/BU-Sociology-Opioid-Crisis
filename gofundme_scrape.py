from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
PATH = "/Users/nikita/chromedriver 2" #update with your Chromedriver path

def get_urls(keywords_list):
    urls = []
    driver = webdriver.Chrome(PATH) 
    for keyword in keywords:
        lastpage = 79 if keyword == 'fentanyl' else 85 #all search results have 85 pages except fentanyl with 79 pages
        for pg in range(1, lastpage):
            sub_url = "https://www.gofundme.com/s?q="+keyword+"&pg="+str(pg)
            driver.get(sub_url)
            html = driver.page_source #parse HTML from Chromedriver
            time.sleep(3)
            parsed_html = BeautifulSoup(html, features="lxml")
            for link in parsed_html.find_all('a', {"class": "a-link a-link--unstyled"}, href=True):
                urls.append('https://www.gofundme.com'+ link['href']) #store links in URL
    print(urls)
    return urls
# keywords = ['opiate']
keywords = ['opiate', 'opioid', 'addiction', 'addict', 'heroin', 'drugs', 'overdose', 
'dependency', 'demon', 'recovery', 'rehabilitation', 'rehab']
get_urls(keywords)




    # keyword = ''
    # pg = ''
    # root_url = "https://www.gofundme.com/s?q="+keyword+"&pg="+pg
    # urls = []
    # campaign_list = []
    # for keyword in keywords:
    #     for pg in range(1, 2):
    #         sub_url = "https://www.gofundme.com/s?q="+keyword+"&pg="+str(pg)
    #         results = requests.get(sub_url).text
    #         parsed_html = BeautifulSoup(results,'html')

    #         for a in parsed_html.find_all('a', href=True):
    #             print(a['href'])
    #         campaign_list = parsed_html.find_all('div', {'class':"m-search-result-skeleton-card m-search-result-card-base mr mb"})
    #         for x in campaign_list:
    #             print(x)
    #         for link in campaign_list:
    #             print(link.a)
    #             urls.append('https://www.gofundme.com'+ link.a['href'])
    #         sub_url = ""
    #         print(urls)
            # results_grid = parsed_html.find('div', {'class':"p-search-results-card-container grid-columns grid-columns--2"})
            # print(results_grid.div)
            # x = results_grid.find("div", {"class": "m-search-result-card m-search-result-card-base mr mb"})
            # print(x.text)

            #class="m-search-result-skeleton-card m-search-result-card-base mr mb"
            
            # for link in campaign_links:
            #     urls.append('https://www.gofundme.com'+ link.a['href'])
            # sub_url = ""
#         return urls


# keywords = ['opiate']
# get_urls(keywords)

# keywords = ['opiate', 'opioid', 'addiction', 'addict', 'heroin', 'drugs', 'overdose', 
# 'dependency', 'demon', 'recovery', 'rehabilitation', 'rehab']