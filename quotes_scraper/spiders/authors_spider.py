import scrapy

class AuthorSpider(scrapy.Spider):
    name = "author-spider"

    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        # Follows links to author pages
        for author in response.css(".author + a::attr(href)"):
            yield response.follow(author, self.parse_author)
        
        # Follows pagination links
        for next_page in response.css("li.next a::attr(href)"):
            yield response.follow(next_page, self.parse)
    
    def parse_author(self, response):
        yield {
            'name': response.css("h3.author-title::text").extract_first().strip(),
            'birthdate': response.css("span.author-born-date::text").extract_first().strip(),
            "description": response.css("div.author-description::text").extract_first().strip(),   
        }