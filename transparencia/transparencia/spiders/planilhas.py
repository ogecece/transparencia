# -*- coding: utf-8 -*-
import scrapy


class PlanilhasSpider(scrapy.Spider):
    name = 'planilhas'
    allowed_domains = ['www.portaltransparencia.gov.br/download-de-dados']
    start_urls = ['http://www.portaltransparencia.gov.br/download-de-dados/']

    def parse(self, response):
        pass
