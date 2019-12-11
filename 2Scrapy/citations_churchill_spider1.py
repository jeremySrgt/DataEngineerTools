import scrapy


class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        for cit in response.css('li.figsco__selection__list__evene__list__item'):
            quote = cit.css('div.figsco__quote__text a::text').get()
            author_path = cit.css('div.figsco__quote__from.figsco__row').css('div.figsco__fake__col-9')
            author = author_path.css('a::text').get()
            yield { 'text' : quote, 'author' : author }
