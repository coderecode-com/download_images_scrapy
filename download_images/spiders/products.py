import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    # allowed_domains = ['x']
    start_urls = ['https://techinstr.myshopify.com/collections/all']

    def parse(self, response):
        for link in response.xpath('//*[contains(@class,"product-card")]/a/@href').getall():
            yield response.follow(link, callback=self.parse_product)
        next_link = response.xpath('//span[contains(text(),"Next page")]/../@href').get()
        if next_link:
            yield response.follow(next_link)

    def parse_product(self, response):
        img_links=[]
        for img in response.xpath('//*[@id="FeaturedImage-product-template"]/@src').getall():
            img_links.append(response.urljoin(img))
            
        yield {
            'title': response.xpath('normalize-space(//h1/text())').get(),
            'price': response.xpath('normalize-space(//*[contains(@class,"price-item--regular")]/text())').get(),
            'image_urls': img_links,
            'Link': response.url
        }
        

