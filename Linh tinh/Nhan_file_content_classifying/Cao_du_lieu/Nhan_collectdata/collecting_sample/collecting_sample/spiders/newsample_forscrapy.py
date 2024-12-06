from scrapy.spiders import CrawlSpider, Rule

from scrapy.linkextractors import LinkExtractor



class CrawlingSpider(CrawlSpider): 
    name = "newcrawler"
    allows_domain = ["toscape.com"]
    start_urls =["http://books.toscrape.com/"]


    rules = (
        Rule(LinkExtractor(allow="catalogue/category")) ,# ", to able recognize as"


        )