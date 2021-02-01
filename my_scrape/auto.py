from time import sleep
import os

while True:
    os.system("cd my_scrape && scrapy crawl App")
    sleep(86400)
