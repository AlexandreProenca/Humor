# -*- coding: utf-8 -*-

from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field
import core.models


class TituloItem(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model = core.models.Titulo
    #title = Field()
    #link = Field()
    #tipo = Field

class EdicaoItem(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model =  core.models.Edicao
    #title = Field()
    #link = Field()
    #tipo = Field