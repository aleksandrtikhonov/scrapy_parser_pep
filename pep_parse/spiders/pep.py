import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response, **kwargs):
        peps_links = response.css('section#numerical-index td a::attr(href)')
        for pep_link in peps_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        data = {
            'number': int(
                response.css('h1.page-title::text').re_first(r'\d+')
            ),
            'name': response.css('h1.page-title::text').get(),
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)
