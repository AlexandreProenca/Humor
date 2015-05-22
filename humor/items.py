# -*- coding: utf-8 -*-

from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field

from core.models import Mensagem


class MensagemItem(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model = Mensagem
    #title = Field()
    #link = Field()
    #tipo = Field
