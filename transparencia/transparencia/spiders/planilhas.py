# -*- coding: utf-8 -*-

import datetime

import scrapy


class PlanilhasSpider(scrapy.Spider):
    name = 'planilhas'
    allowed_domains = ['www.portaltransparencia.gov.br']
    start_urls = ['http://www.portaltransparencia.gov.br/download-de-dados/']
    optional_args = ['all']

    def parse(self, response):
        yield scrapy.http.Request(
            url=response.url + 'transferencias/',
            callback=self.baixa_planilhas,
        )

    def baixa_planilhas(self, response):
        if hasattr(self, 'all'):
            disponiveis = anos_meses(response)
        else:
            hoje = datetime.date.today()
            disponiveis = [(str(hoje.year), str(hoje.month))]

        for ano_mes in disponiveis:
            yield {'file_urls': [response.url + ''.join(ano_mes)]}


def anos_meses(response):
    todos = response.xpath('//script').re(r'arquivos\.push.+?(\d{4}).+?(\d{2})')
    return agrupador(todos, 2)


def agrupador(iteravel, n):
    '''Agrupa dados em blocos de tamanho fixo

    Exemplos:
        >>> agrupador('ABCDEFGHI', 3)
        'ABC' 'DEF' 'GHI'
    '''
    args = [iter(iteravel)] * n
    return zip(*args)
