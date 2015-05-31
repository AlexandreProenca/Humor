# from scrapy.contrib.spiders import CrawlSpider
# from humor.items import MensagemItem
# from scrapy.selector import Selector
# from scrapy.http import Request
# import itertools
# import time
#
# class Jokes4UsSpider(CrawlSpider):
#     name = 'joke'
#     allowed_domains = ['videosengracados.blog.br']
#     start_urls = ['http://videosengracados.blog.br/videoscategory/legais/',
#                   'http://videosengracados.blog.br/videoscategory/legais/page/2/',
#                   'http://videosengracados.blog.br/videoscategory/legais/page/3/',
#                   'http://videosengracados.blog.br/videoscategory/legais/page/4/',
#                   'http://videosengracados.blog.br/videoscategory/legais/page/5/',
#                   'http://videosengracados.blog.br/videoscategory/legais/page/6/',
#                   'http://videosengracados.blog.br/videoscategory/legais/page/7/',
#                   'http://videosengracados.blog.br/videoscategory/legais/page/8/']
#
#     def parse(self, response):
#         sel = Selector(response)
#         links = sel.xpath('//iframe')
#         url = links[0].xpath('//div[@class="view-img"]/a/@href').extract()
#         for r in url:
#             print r
#             time.sleep(1)
#             yield(Request(r, callback = self.parse_iframe))
#
#
#     def parse_iframe(self, response):
#         sel = Selector(response)
#         links = sel.xpath('//div')
#         link = links[0].xpath('//*[@id="main"]/article/div/div/iframe/@src').extract()
#         #title = links[0].xpath('//*[@id="main"]/article/div/h3/text()').extract()
#         title = links[0].xpath('//*[@id="main"]/header/div/h1/text()').extract()
#         items = []
#         for l,t in itertools.izip(link, title):
#              item = MensagemItem()
#              you_id = l.split('/')[4].split('?')[0]
#              youtube_link = "https://www.youtube.com/watch?v="+you_id
#              item['link'] = youtube_link
#              item['titulo'] = t
#              item['tipo'] = "VIDEO"
#              items.append(item)
#         return items
