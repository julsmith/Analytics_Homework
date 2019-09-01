from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import os

def scrape_info():
    executable_path = {"executable_path": "chromedriver.exe"}
    browser =  Browser("chrome", **executable_path, headless=False)
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    news_title = soup.find('div', class_= 'content_title').text
    news_paragragh = soup.find('div', class_= 'article_teaser_body').text

    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    browser.click_link_by_partial_text("FULL IMAGE")
    time.sleep(5)
    browser.click_link_by_partial_text("more info")
    time.sleep(5)
    featured_page = browser.html
    image_soup = bs(featured_page, "html.parser")

    featured_img = image_soup.find('figure', class_= "lede")
    featured_img_url = featured_img.a["href"]
    featured_img_url = ("https://www.jpl.nasa.gov" + featured_img_url)
    print("featured image url")
    print(featured_img_url)


    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    html_weather = browser.html
    soup = bs(html_weather, 'html.parser')

    mars_weather = soup.find("p", class_= "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text.strip()
    print("================")
    print(mars_weather)
    print("================")

   # facts_url = 'https://space-facts.com/mars/'
    #mars_facts = pd.read_html(facts_url)


   # mars_df = mars_facts[1]
    #mars_df.columns = ['Description','Value']
    #mars_df.set_index('Description', inplace=True)
    #data = mars_df.to_dict(orient='records')



    hemph_img_urls = []
    hemph_dictionary = {"title": [] , "img_url": []}
    hemph_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser = Browser("chrome", headless = False)
    browser.visit(hemph_url)
    time.sleep(3)
    home = browser.html
    hemph_soup = bs(home, "html.parser")
    results = hemph_soup.find_all("h3")
    for result in results:
        title = result.text[:-9]
        print(title)
        browser.click_link_by_partial_text(title)
        time.sleep(3)
        img_url = browser.find_link_by_partial_href("download")["href"]
        print(img_url)
        hemph_dictionary = {"title": title, "img_url": img_url}
        hemph_img_urls.append(hemph_dictionary)
        time.sleep(3)
        browser.visit(hemph_url)
    final_dict = {"news_title": news_title, "news_paragraph": news_paragragh, 
    "imageURL": featured_img_url, "mars_weather": mars_weather, "hemp_images": hemph_img_urls
    }

    return final_dict



