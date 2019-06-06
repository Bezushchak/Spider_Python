import scrapy

class QuotesSpider(scrapy.Spider):
    name = "table_scrape"

    def start_requests(self):
        urls = [
            'https://imi.org.ua/monitoring-types/doslidzhennya-dzhynsy/page/1/',
            'https://imi.org.ua/monitoring-types/doslidzhennya-dzhynsy/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'table_scrape-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file%s' % filename)
