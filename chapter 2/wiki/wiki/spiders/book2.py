import scrapy

class Book2Spider(scrapy.Spider):
    name = 'book2'
    start_urls = [
        'http://wikibook.co.kr/list/'
    ]

    def parse(self, response):
        # 도서 목록 추출하기
        li_list = response.css('.book-url')
        for a in li_list:
            href = a.css('::attr(href)').extract_first()
            text = a.css('::text').extract_first()

            href2 = response.urljoin(href)

            yield {
                'text' : text,
                'url' : href
            }

# wiki > wiki > spiders에서 
# scrapy crawl book2 -o list.json