import scrapy
import requests

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        quotes = []
        for quote in response.css('div.quote'):
            quote_data = {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
            }
            quotes.append(quote_data)

        self.send_quotes(quotes)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def send_quotes(self, quotes):

        backend_url = 'http://127.0.0.1:5000/quotes'

        response = requests.post(backend_url, json=quotes)

        if response.status_code == 200:
            self.logger.info('Scraped quotes sent to the backend successfully.')
        else:
            self.logger.error(f'Failed to send quotes to the backend. Status code: {response.status_code}')

