# -*- coding: utf-8 -*-

# Scrapy settings for humor project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
# Setting up django's project full path.
import sys
#sys.path.insert(0, '/home/ec2-user/projetos/ambiente_risada/risada')
sys.path.insert(0, '/Users/thod/PycharmProjects/seed-backend-python/ambiente_revistaria/revistaria')

# Setting up django's settings module name.
# This module is located at /home/rolando/projects/myweb/myweb/settings.py.
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'revistaria.settings'

BOT_NAME = 'humor'

SPIDER_MODULES = ['humor.spiders']
NEWSPIDER_MODULE = 'humor.spiders'


ITEM_PIPELINES = {
    'humor.pipelines.HumorPipeline': 1000,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'humor (+http://www.yourdomain.com)'
