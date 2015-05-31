# coding: utf-8
from humor.items import EdicaoItem
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request

class DmozSpider(CrawlSpider):
    name = "panini"
    allowed_domains = ["paninicomics.com.br"]
    start_urls = [
        "http://www.paninicomics.com.br/web/guest/marvel/titulos",
        "http://www.paninicomics.com.br/web/guest/dc/titulos",
        "http://www.paninicomics.com.br/web/guest/manga/titulos",
    ]

    def parse(self, response):
        sel = Selector(response)
        url = sel.xpath('//div/div/div/ul/li/a/@href').extract()
        for r in url:
            titulo_link = "http://www.paninicomics.com.br"+r
            yield(Request(titulo_link, callback = self.second_link))


    def second_link(self, response):
        sel = Selector(response)
        url = sel.xpath('//*[@id="shop"]/div/div/div/h3/a/@href').extract()
        for r in url:
            revista_link = "http://www.paninicomics.com.br"+r
            yield(Request(revista_link, callback = self.parse_iframe))


    def parse_iframe(self, response):
        sel = Selector(response)
        links = sel.xpath('//div')
        item = EdicaoItem()
        item['nome'] = links[0].xpath('//*[@id="shop"]/div[1]/h1/text()').extract()[0]
        item['imagem'] = "http://www.paninicomics.com.br"+str(links[0].xpath('//*[@id="shop"]/div[2]/div[1]/img/@src').extract()[0])
        item['data'] = links[0].xpath('//*[@id="shop"]/div[2]/div[4]/p/strong/text()').extract()[0]
        item['valor'] = float(links[0].xpath('//*[@id="shop"]/div[2]/div[4]/h3/strong/text()').extract()[0])
        try:
            item['descricao'] = links[0].xpath('//*[@id="shop"]/div[2]/div[6]/p[1]/text()').extract()[0]
        except:
            item['descricao'] = "Sem Descrição"
        return item
