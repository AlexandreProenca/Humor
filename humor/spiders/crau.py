from scrapy.spider import Spider
from scrapy.selector import Selector
from humor.items import MensagemItem
import itertools

class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["anoesemchamas.com.br"]
    start_urls = [
        "http://www.anoesemchamas.com.br/",
        "http://www.anoesemchamas.com.br/page/2/",
        "http://www.anoesemchamas.com.br/page/3/",
        "http://www.anoesemchamas.com.br/page/4/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        links = sel.xpath('//iframe')
        items = []

        link = links[0].xpath('//iframe/@src').extract()
        title = links[0].xpath('//h2/a/text()').extract()
        for l,t in itertools.izip(link, title):
             item = MensagemItem()
             item['link'] = l
             item['titulo'] = t
             item['tipo'] = "VIDEO"
             items.append(item)
        return items
