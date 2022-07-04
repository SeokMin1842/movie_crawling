from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()

options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver.exe')

# https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020&page=1 ~ 37까지
# //*[@id="old_content"]/ul/li[1]/a                     title
# //*[@id="old_content"]/ul/li[2]/a
# //*[@id="old_content"]/ul/li[20]/a
# //*[@id="reviewTab"]/div/div/ul/li[1]/a               review tab
# //*[@id="reviewTab"]/div/div/ul/li[10]/a
# //*[@id="pagerTagAnchor1"]/span
# //*[@id="pagerTagAnchor2"]/span
# //*[@id="pagerTagAnchor3"]/span
# //*[@id="pagerTagAnchor10"]/span
# //*[@id="pagerTagAnchor11"]/span

review_number_xpath = '//*[@id="movieEndTabMenu"]/li[6]/a'

for i in range(1, 38):
    url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2020&page={}'.format(i)
    titles = []
    reviews = []
    try:
        driver.get(url)
        time.sleep(0.1)
        for j in range(1, 21):
            movie_title_xpath = '//*[@id="old_content"]/ul/li[{}]/a'.format(j)
            try:
                title = driver.find_element("xpath", movie_title_xpath).text
                driver.find_element("xpath", movie_title_xpath).click()
                time.sleep(0.1)
                driver.find_element('xpath', review_number_xpath).click()
                time.sleep(0.1)
                review_range = driver.find_element('xpath', review_number_xpath).text
                review_range = review_range.replace(',', '')
                review_range = (int(review_range)-1) // 10 + 2
                for k in range(1, review_range):
                    review_page_button_xpath = '//*[@id="pagerTagAnchor{}"]'.format(k)
                    for l in range(1, 11):
                        review_title_xpath = '//*[@id="reviewTab"]/div/div/ul/li[{}]/a'.format(l)
                        try:
                            review = driver.find_element('xpath', review_title_xpath).click()
                            time.sleep(0.1)
                            review = driver.find_element('xpath', review_xpath).text
                            print(title)
                            print(review)
                            driver.back()
                        except:
                            print('review', i, j, k)
                    driver.back()
                except:
                    print('review page', i, j, k)
            except:
                print('movie', i, j)
    except:
        print('page', i)
    finally:
        pass
        driver.close()

