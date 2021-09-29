# virtuallenv_scrapy

scrapy shell "https://www.deutsches-krankenhaus-verzeichnis.de/app/suche/bundesland/sachsen"
response
table = response.xpath('//*[@class="table table-striped table-bordered table-hover"]')
table
table = response.xpath('//*[@class="table table-striped table-bordered table-hover"]//tbody')
table
table.xpath('//tr')
response.xpath('//*[@class="table table-striped table-bordered table-hover"]//tbody//tr//td//address//strong//a')


following links: https://docs.scrapy.org/en/latest/topics/developer-tools.html

https://docs.scrapy.org/en/latest/intro/tutorial.html
