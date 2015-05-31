# #-*- coding: utf-8 -*-
# from humor.items import MensagemItem
# from scrapy.spider import Spider
# from scrapy.selector import Selector
# from urlparse import urljoin
# from scrapy import Request
# import itertools
#
#
# class DmozSpider(Spider):
#     name = "virgula"
#     allowed_domains = ["uhull.virgula.uol.com.br"]
#     start_urls = (
#         'http://uhull.virgula.uol.com.br/',
#         'http://uhull.virgula.uol.com.br/page/2/',
#         'http://uhull.virgula.uol.com.br/page/3/',
#         'http://uhull.virgula.uol.com.br/page/4/',
#         'http://uhull.virgula.uol.com.br/page/5/',
#         'http://uhull.virgula.uol.com.br/page/6/',
#         'http://uhull.virgula.uol.com.br/page/7/',
#         'http://uhull.virgula.uol.com.br/page/8/',
#         'http://uhull.virgula.uol.com.br/page/10/',
#         'http://uhull.virgula.uol.com.br/page/11/',
#         'http://uhull.virgula.uol.com.br/page/12/',
#         'http://uhull.virgula.uol.com.br/page/13/',
#         'http://uhull.virgula.uol.com.br/page/14/',
#         'http://uhull.virgula.uol.com.br/page/16/',
#     )
#
#
#     def parse(self, response):
#         """
#         The lines below is a spider contract. For more info see:
#         http://doc.scrapy.org/en/latest/topics/contracts.html
#         @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
#         @scrapes name
#         """
#         sel = Selector(response)
#         links = sel.xpath('//iframe')
#         items = []
#
#         #link = links.xpath('//div/div/a/@href').extract()
#         link = links[0].xpath('//iframe/@src').extract()
#         title = links[0].xpath('//h2/a/text()').extract()
#
#         for l,t in itertools.izip(link, title):
#              item = MensagemItem()
#              you_id = l.split('/')[4].split('?')[0]
#              youtube_link = "https://www.youtube.com/watch?v="+you_id
#              item['link'] = youtube_link
#              item['titulo'] = t
#              item['tipo'] = "VIDEO"
#              items.append(item)
#         return items
