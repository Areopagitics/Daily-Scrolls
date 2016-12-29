import re
import scrapy
from scrapy.item import Item, Field
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import HtmlXPathSelector
from scrapy_webdriver.http import WebdriverRequest

from selenium import webdriver


class ReadingsItem(Item):
    Acclamation = Field()
    SecondReading = Field()
    Psalm = Field()
    FirstReading = Field()
    Date = Field()
    Gospel = Field()
    Day = Field()


class MySpider(scrapy.Spider):
    name = 'readings'
    #download_delay = 2
    allowed_domains = ['ewtn.com']

    def start_requests(self):
        urls = [
            'http://www.ewtn.com/daily-readings/?date=2016-12-24',
'http://www.ewtn.com/daily-readings/?date=2016-12-25',
'http://www.ewtn.com/daily-readings/?date=2016-12-26',
'http://www.ewtn.com/daily-readings/?date=2016-12-27',
'http://www.ewtn.com/daily-readings/?date=2016-12-28',
'http://www.ewtn.com/daily-readings/?date=2016-12-29',
'http://www.ewtn.com/daily-readings/?date=2016-12-30',
'http://www.ewtn.com/daily-readings/?date=2016-12-31',




     

        ]
        for url in urls:
            yield WebdriverRequest(url=url, callback=self.parse)
    
    def parse(self, response):        
        
        item = ReadingsItem()
        item["Day"] = response.xpath('//div[@class="day-title"]/text()').extract()
        item["Date"] = response.url.split('=')[-1]

    
        readings = {'First Reading':'FirstReading', 'Responsorial Psalm':'Psalm', 'Second Reading':'SecondReading', 'Verse Before':'Acclamation', 'Alleluia':'Acclamation', 'Gospel':'Gospel'}
        passages = response.xpath('//div[@class="reference hanging"]/text()').extract()
        titles = response.xpath('//div[@class="reading-type"]/text()').extract()
        print titles
        for r,i in readings.iteritems():
            for f in titles:
                if r in f:
                    n = titles.index(f)
                    item[i] = passages[n]                
        return item 
    """                        
        self.driver.close()


        
    def parse(self, response):
        item = ReadingsItem()
        Acclamation,SecondReading,Psalm,FirstReading,Date,Gospel,Day
        item["day"] = response.xpath('//h3/text()')[2].extract()
        item["date"] = response.xpath('//h1/text()')[0].extract()
        item["first_reading"] = response.xpath('//div[@class="bibleReadingsWrapper"]/div[@class="pane current"]/h4/a/text()')[0].extract()
        item["psalm"] = response.xpath('//div[@class="bibleReadingsWrapper"]/div[@class="poetry"]/h4/a/text()')[1].extract()
        item["second_reading"] = response.xpath('//div[@class="bibleReadingsWrapper"]/div[@class="poetry"]/h4/a/text()')[2].extract()
        item["alleluia"] = response.xpath('//div[@class="bibleReadingsWrapper"]/div[@class="poetry"]/h4/a/text()')[3].extract()
        item["gospel"] = response.xpath('//div[@class="bibleReadingsWrapper"]/div[@class="poetry"]/h4/a/text()')[4].extract()
        return item 
       
        
 
    start_urls = [
        'http://www.usccb.org/bible/readings/092417.cfm',
      
    ]
        def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
from scrapy_webdriver.http import WebdriverRequest
        for url in urls:
            yield WebdriverRequest(url=url, callback=self.parse)

    def parse(self, response):
        dweeks = response.xpath('//h3').extract()
        dates = response.xpath('//h1').extract()
        readings = response.xpath('//h4').extract()
        items = []
        for dweek in dweeks:
            item = ReadingsItem()
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            for day in days:
                if dweek.find(day):
                    item["day"] = day
                    if day == 'Sunday':
                        dweek.replace(day, 'Week')
                stoplist = ('of', 'the')
                for s in stoplist:
                    dweek.replace(s, '')
                    item["week"] = dweek
            items.append(item)
        return items


response.xpath('//div[@id="navDates"]/a/text()')[1].extract()
    links = response.xpath('//a[@class="hdrlnk"]/@href').extract()


        for dweek in dweeks:
            item = ReadingsItem()
            item["week"] = dweek.select("a/dweek()").extract()
            item["day"] = dweek.select("a/@href").extract()
            items.append(item)
        return items

        """
