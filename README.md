# Quotes Scraper Using Scrapy

## Intro

A Web Scraper that uses Python3 and Scrapy to scrape [Quotes To Scrape](http://quotes.toscrape.com/). 

Includes 2 spiders: 

* [quotes-spider](./quotes_scraper/spiders/quotes_spider.py) crawls and retrieves all quotes with the author and tags.
* [author-spider](./quotes_scraper/spiders/authors_spider.py) crawls and retrieves all author details including name, DOB and description.

## Requirements

* Python 3.x
* Scrapy

## Usage

    scrapy crawl quote-spider > quotes.json
    scrapy crawl author-spider > authos.json

Example output JSON files are [here](./example-output).

## Caveat

Example output has been beautified with [JSON Lint](https://jsonlint.com/) for readability.

Working of this web scraper depends on the source at [Quotes To Scrape](http://quotes.toscrape.com/). 

Foundation for this scraper can be found [here](https://doc.scrapy.org/en/latest/intro/tutorial.html).
