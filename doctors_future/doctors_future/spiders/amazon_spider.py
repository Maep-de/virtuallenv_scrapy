# This package will contain the spiders of your Scrapy project

#

import scrapy
#from ..items import AmazonItem


class AmazonSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):
        urls = [
            'https://www.amazon.de/-/en/gp/bestsellers/fashion/1760237031/ref=zg_bs_nav_2_12419317031'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    #start_urls = ['']


    def parse(self, response):
        #items = AmazonItem();
        #product_name = response.css().extract('p13n-sc-truncated::text');
        #product_price = response.css().extract('p13n-sc-price::text');
        #items['product_name'] = product_name;
       # items['product_price'] = product_price;
        #yield items;
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


# Please refer to the documentation for information on how to create and manage
# your spiders.
