#-*- coding: utf-8 -*-
from humor.items import HumorItem
from scrapy.spider import Spider
from scrapy.selector import Selector
import itertools


class DmozSpider(Spider):
    name = "humorcombobagem"
    allowed_domains = ["humorcombobagem.com"]
    start_urls = (
        'http://www.humorcombobagem.com/categoria/besteirol.html',
        'http://www.humorcombobagem.com/categoria/coisas-de-macho.html',
        'http://www.humorcombobagem.com/categoria/bebados.html',
        'http://www.humorcombobagem.com/categoria/beleza-interior.html',
        'http://www.humorcombobagem.com/categoria/burrices-e-idiotices.html',
        'http://www.humorcombobagem.com/categoria/manolo.html',
        'http://www.humorcombobagem.com/categoria/politicos.html',
        'http://www.humorcombobagem.com/categoria/caras-e-caretas.html',
        'http://www.humorcombobagem.com/categoria/charadas.html',
        'http://www.humorcombobagem.com/categoria/charges-e-quadrinhos.html',
        'http://www.humorcombobagem.com/categoria/comerciais.html',
        'http://www.humorcombobagem.com/categoria/como-as-pessoas-veem.html',
        'http://www.humorcombobagem.com/categoria/compartilhe!.html',
        'http://www.humorcombobagem.com/categoria/dorgas-mano.html',
        'http://www.humorcombobagem.com/categoria/esporte.html',
        'http://www.humorcombobagem.com/categoria/face-maldicao.html',
        'http://www.humorcombobagem.com/categoria/face-okay.html',
        'http://www.humorcombobagem.com/categoria/fail.html',
        'http://www.humorcombobagem.com/categoria/fazendo-errado.html',
        'http://www.humorcombobagem.com/categoria/forever-alone.html',
        'http://www.humorcombobagem.com/categoria/fotos-engracadas.html',
        'http://www.humorcombobagem.com/categoria/frases-e-pensamentos.html',
        'http://www.humorcombobagem.com/categoria/fuck-yeah.html',
        'http://www.humorcombobagem.com/categoria/gambiarra.html',
        'http://www.humorcombobagem.com/categoria/graficos-da-vida.html',
        'http://www.humorcombobagem.com/categoria/historinhas.html',
        'http://www.humorcombobagem.com/categoria/homens-x-mulheres.html',
        'http://www.humorcombobagem.com/categoria/imagens-topicos-do-orkut.html',
        'http://www.humorcombobagem.com/categoria/mestres-do-photoshop.html',
        'http://www.humorcombobagem.com/categoria/mundo-invisivel.html',
        'http://www.humorcombobagem.com/categoria/nerds.html',
        'http://www.humorcombobagem.com/categoria/noticias-de-duplo-sentido.html',
        'http://www.humorcombobagem.com/categoria/o-que-foi-que-eu-fiz.html',
        'http://www.humorcombobagem.com/categoria/pervertidos.html',
        'http://www.humorcombobagem.com/categoria/piadas.html',
        'http://www.humorcombobagem.com/categoria/placas-e-avisos.html',
        'http://www.humorcombobagem.com/categoria/pobre-x-rico.html',
        'http://www.humorcombobagem.com/categoria/poker-face.html',
        'http://www.humorcombobagem.com/categoria/prints-do-facebook.html',
        'http://www.humorcombobagem.com/categoria/prints-do-msn.html',
        'http://www.humorcombobagem.com/categoria/prints-do-orkut.html',
        'http://www.humorcombobagem.com/categoria/prints-do-twitter.html',
        'http://www.humorcombobagem.com/categoria/quando-perceber-vai-rir.html',
        'http://www.humorcombobagem.com/categoria/qui-issu-jovem.html',
        'http://www.humorcombobagem.com/categoria/semelhancas.html',
        'http://www.humorcombobagem.com/categoria/tenso.html',
        'http://www.humorcombobagem.com/categoria/trollando.html',
        'http://www.humorcombobagem.com/categoria/wtf.html',
    )

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        links = sel.xpath('//a/img[@class="img_unica"]')
        items = []

        link = links[0].xpath('//a/img[@class="img_unica"]/@src').extract()
        title = links[0].xpath('//h2/a/text()').extract()
        for l,t in itertools.izip(link, title):
             item = HumorItem()
             item['link'] = l
             item['title'] = t
             items.append(item)
        return items
