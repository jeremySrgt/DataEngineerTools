import requests
from random import *
from bs4 import BeautifulSoup
import json


class ReqHTTP:
    def __init__(self, url,timeout=10):
        self.url = url
        self.timeout = timeout

    def getContent(self):
        userAgent = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"
        ]

        rand = randint(0,len(userAgent)-1)

        headers = {'User-Agent': userAgent[rand]}
        response = requests.get(self.url, headers = headers, timeout=self.timeout)
        if(response.status_code == 200):
            return response.text
        else:
            return response.status_code

    def del_space(self, string):
        remove_lt_space = string.strip()
        remove_double_spacing =remove_lt_space.replace('  ', ' ')
        return remove_double_spacing


    def get_soup(self):
        return BeautifulSoup(self.getContent(),'xml')

    def get_links(self):
        soup = self.get_soup()
        a_tag = soup.find_all("a")
       
        links_dict = {i: i.get('href') for i in a_tag}
        return links_dict

    def create_json(self):
        soup = self.get_soup()
        items = soup.find_all("item")
        title = [i.title.text for i in items]
        description = [i.description.text for i in items]
        url = [i.link.text for i in items ]
        img = [i.enclosure.get('url') for i in items]


        create_dict = [{"title" : title[index], "description": description[index], "url" : url[index]} for index,element in enumerate(items)]






if __name__ == "__main__":
    scraping = ReqHTTP("https://www.lemonde.fr/jeux-video/rss_full.xml")
    scraping.create_json()
    


