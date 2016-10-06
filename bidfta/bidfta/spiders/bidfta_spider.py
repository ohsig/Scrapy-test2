from scrapy import Spider

class bidftaSpider(Spider):
    name = "bidffta"
    allow_domains = ["bidfta.com"]
    start_urls = [
        "http://www.bidfta.com/"
    ]