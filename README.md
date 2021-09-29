# virtuallenv_scrapy

Following Link: https://docs.scrapy.org/en/latest/intro/tutorial.html

installation with anaconda: conda install -c conda-forge scrapy

create : https://docs.scrapy.org/en/latest/intro/tutorial.html
scrapy startproject DoctorsFuture
C:\Users\Dell\anaconda3\Lib\site-packages\scrapy\templates\project
C:\Users\Dell\tutorial1


error: ModuleNotFoundError: No module named 'Protego'

from anaconda: pip install Protego

https://nomodulenamed.com/m/protego

pip problem
Update pip: pip install --upgrade pip

to keep data: scrapy crawl quotes


scrapy shell "https://www.deutsches-krankenhaus-verzeichnis.de/app/suche/bundesland/sachsen"

response

table = response.xpath('//*[@class="table table-striped table-bordered table-hover"]')

table

table = response.xpath('//*[@class="table table-striped table-bordered table-hover"]//tbody')

table

table.xpath('//tr')

response.xpath('//*[@class="table table-striped table-bordered table-hover"]//tbody//tr//td//address//strong//a')




<br/><br/>
following links: https://docs.scrapy.org/en/latest/topics/developer-tools.html


https://docs.scrapy.org/en/latest/intro/tutorial.html
