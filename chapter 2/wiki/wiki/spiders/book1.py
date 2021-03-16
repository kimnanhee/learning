import scrapy

class Book1Spider(scrapy.Spider):
    name = 'book'
    start_urls = [
        'http://wikibook.co.kr/list/'
    ]

    def parse(self, response):
        # 도서 목록 추출하기
        title = response.css('title')
        print(title.extract())

# wiki > wiki > spiders에서 
# scrapy crawl book --nolog