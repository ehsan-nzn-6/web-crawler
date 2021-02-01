import scrapy
import os
from datetime import datetime


class QuotesSpider(scrapy.Spider):
    name = "App"

    def start_requests(self):
        urls = [
            "https://www.bprshop.com/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        name_xpath = "/html/body/div[1]/section/div/div/div/div[2]/div/div/div/table/tbody/tr[{}]/td[2]/a/text()"
        price_xpath = "/html/body/div[1]/section/div/div/div/div[2]/div/div/div/table/tbody/tr[{}]/td[12]/text()"
        result = []
        name_list = []
        price_list = []
        try:
            for i in range(1, 999):
                name = response.xpath(name_xpath.format(i)).get()
                if name != None:
                    name_list.append(name)
                price = response.xpath(price_xpath.format(i)).get()
                if name != None:
                    price_list.append(price)
                result.append(price)
        except:
            pass
        price_list = list(map(lambda i: i.replace(",", ""), price_list))
        price_list = list(map(lambda i: i.replace("\t", ""), price_list))
        data = zip(name_list, price_list)
        try:
            os.mkdir("data")
        except:
            pass
        date = datetime.now()
        for i, j in data:
            with open(f"./data/{i}.csv", "a", encoding="utf-8") as f:
                f.write(f"{j},{date}\n")
