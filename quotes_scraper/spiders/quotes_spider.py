import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quote-spider"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first().replace("\u201c",""),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags a.tag::text").extract(),
            }
        next_page = response.css("li.next a::attr(href)").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)