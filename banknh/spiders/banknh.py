import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from banknh.items import Article


class BanknhSpider(scrapy.Spider):
    name = 'banknh'
    start_urls = ['https://www.banknh.com/about/news-room?year=']

    def parse(self, response):
        links = response.xpath('//li[@class="year "]/a/@href').getall()
        yield from response.follow_all(links, self.parse_year)

    def parse_year(self, response):
        articles = response.xpath('//div[@class="press-release-item"]')
        for article in articles:
            link = article.xpath('.//a/@href').get()
            date = article.xpath('./p/text()').get().strip()
            yield response.follow(link, self.parse_article, cb_kwargs=dict(date=date))

    def parse_article(self, response, date):
        if 'pdf' in response.url:
            return

        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//div[@class="press-release"]/h1/text()').get()
        if title:
            title = title.strip()

        content = response.xpath('//div[@class="press-release"]//text()').getall()
        content = [text for text in content if text.strip()]
        content = "\n".join(content[1:]).strip()

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
