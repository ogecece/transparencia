# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from transparencia.transparencia import settings
from transparencia.transparencia.spiders.planilhas import PlanilhasSpider

project_settings = Settings()
project_settings.setmodule(settings)
process = CrawlerProcess(project_settings)
# process.crawl(PlanilhasSpider, all=True)
process.crawl(PlanilhasSpider)
process.start()
