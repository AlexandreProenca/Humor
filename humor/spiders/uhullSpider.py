#-*- coding: utf-8 -*-
from humor.items import MensagemItem 
from scrapy.spider import Spider
from scrapy.selector import Selector
import itertools


class DmozSpider(Spider):
    name = "videose"
    #allowed_domains = ["uhull.virgula.uol.com.br"]
    allowed_domains = ["http://videosengracados.blog.br/"]
    start_urls = (
        #'http://uhull.virgula.uol.com.br/',
	'http://videosengracados.blog.br/videos/',
    
    )

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        #links = sel.xpath('//div[@class="html5-title"]')
        
	links= sel.xpath('//div')
	items = []

        ##link = links.xpath('//div/div/a/@href').extract()
        #link = links[0].xpath('//div/a/@href').extract()
        
	link = links[0].xpath('//iframe/@src').extract()
	##link = links.xpath('//div/a/@href').extract()
        title = links[0].xpath('//h2/a/text()').extract()
        for l,t in itertools.izip(link, title):
             item = MensagemItem()
             item['link'] = l
             item['titulo'] = t
             item['tipo'] = "VIDEO"
             items.append(item)
        return items
