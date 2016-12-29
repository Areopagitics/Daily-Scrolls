import re
import scrapy
from scrapy.item import Item, Field
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import HtmlXPathSelector
from scrapy_webdriver.http import WebdriverRequest

from selenium import webdriver


class ReadingsItem(Item):
    Book = Field()
    Chapter = Field()
    Verse = Field()
    Word = Field()
    Original = Field()
    Translation = Field()


class MySpider(scrapy.Spider):
    name = 'readings'
    #download_delay = 2
    allowed_domains = ['en.katabiblon.com']
    start_urls = [

'http://en.katabiblon.com/us/index.php?text=LXX&book=Sir&ch=1',


    ]

    def parse(self, response):
        item = ReadingsItem()
        item["Book"] = response.url.split('book=')[-1][:3]
        item["Chapter"] = response.url.split('ch=')[-1]
        verses = len(response.xpath('//td[@class="c1"]'))
        for n in range(1,verses+1):
            item["Verse"] = n
            words = response.xpath('//tr[@id="v'+str(n)+'"]/td[@lang="el-polyton"]/text()').extract()
            inum = 1
            anum = 1
            for w in words:
                item["Original"] = response.xpath('//tr[@id="v'+str(n)+'"]/td/span[@class="interlinear"]['+str(inum)+']/span/text()').extract()
                try:
                    t = response.xpath('//tr[@id="v'+str(n)+'"]/td/span[@class="interlinear"]['+str(inum)+']/span/span[@class="popup"]/span[@lang="en" and position() = last()]/text()').extract()[1]
                    item["Translation"] = re.search(r'\w+(\s[a-z]+)?', t).group()
                except:
                    pass
                item["Word"] = anum
                anum += 1
                inum += 1
                yield item

                item["Translation"] = " "
                item["Original"] = " "

                if w!=" ":
                    item["Translation"] = " "
                    item["Original"] = w
                    item["Word"] = anum
                    yield item
                    anum += 1

            vs = len(words)+1+len([w for w in words if w!=" "])
            if anum<=vs:
                try:
                    item["Original"] = response.xpath('//tr[@id="v'+str(n)+'"]/td/span[@class="interlinear"]['+str(inum)+']/span/text()').extract()
                    try:
                        t = response.xpath('//tr[@id="v'+str(n)+'"]/td/span[@class="interlinear"]['+str(inum)+']/span/span[@class="popup"]/span[@lang="en" and position() = last()]/text()').extract()[1]
                        item["Translation"] = re.search(r'\w+(\s[a-z]+)?', t).group()
                    except:
                        pass
                    item["Word"] = anum
                    yield item
                except:
                    pass

        base = 'http://en.katabiblon.com/us/'
        url = response.xpath('//a[@class="next-arrow"]/@href')[0].extract()
        yield scrapy.Request(base+url, callback=self.parse)




    """
----------------------------------

scrapy crawl readings -o test.csv

scrapy shell "http://en.katabiblon.com/us/index.php?text=LXX&book=Wsd&ch=4"
------------------------------------


TRYING TO FILTER OUT WEIRD SYMBOLS BELOW

class MySpider(scrapy.Spider):
    name = 'readings'
    #download_delay = 2
    allowed_domains = ['en.katabiblon.com']
    start_urls = [
'http://en.katabiblon.com/us/index.php?text=LXX&book=Jdt&ch=16',


    ]

    def parse(self, response):
        item = ReadingsItem()
        item["Book"] = response.url.split('book=')[-1][:3]
        item["Chapter"] = response.url.split('ch=')[-1]
        verses = len(response.xpath('//td[@class="c1"]'))
        for n in range(1,verses+1):
            item["Verse"] = n
            words = response.xpath('//tr[@id="v'+str(n)+'"]/td[@lang="el-polyton"]/text()').extract()
            inum = 1
            anum = 1
            uw = [u'\x04',u'\x14',"{","}"]
            for w in words:
                item["Original"] = response.xpath('//tr[@id="v'+str(n)+'"]/td/span[@class="interlinear"]['+str(inum)+']/span/text()').extract()
                try:
                    t = response.xpath('//tr[@id="v'+str(n)+'"]/td/span[@class="interlinear"]['+str(inum)+']/span/span[@class="popup"]/span[@lang="en" and position() = last()]/text()').extract()[1]
                    item["Translation"] = re.search(r'\w+(\s[a-z]+)?', t).group()
                except:
                    pass
                item["Word"] = anum
                anum += 1
                inum += 1
                if any(x in t for x in uw) or t==" ":
                    continue
                yield item

                try:
                    swords = response.xpath('//tr[@id="v'+str(n)+'"]/td[@lang="el-polyton"]/span[@class="interlinear"]['+str(inum)+']/span[@class="shadow"]/text()').extract()
                    sinum = 1
                    for s in swords:
                        item["Original"] = response.xpath('//tr[@id="v'+str(n)+'"]/td/span[@class="interlinear"]['+str(inum)+']/span/span[@class="interlinear"]['+str(sinum)+']/text()').extract()
                        try:
                            t = response.xpath('//tr[@id="v'+str(n)+'"]/td/span[@class="interlinear"]['+str(inum)+']/span/span[@class="interlinear"]['+str(sinum)+']/span[@class="popup"]/span[@lang="en" and position() = last()]/text()').extract()[1]
                            item["Translation"] = re.search(r'\w+(\s[a-z]+)?', t).group()
                        except:
                            pass
                        item["Word"] = anum
                        anum += 1
                        sinum += 1
                        yield item

                        item["Translation"] = " "
                        item["Original"] = " "

                        if s!=" ":
                            item["Translation"] = " "
                            item["Original"] = s
                            item["Word"] = anum
                            yield item
                            anum += 1
                    vs = len(words)+1+len([s for s in swords if s!=" "])
                    if anum<=vs:
                        try:
                            item["Original"] = response.xpath('//tr[@id="v'+str(n)+'"]/td/span[@class="interlinear"]['+str(inum)+']/span/span[@class="interlinear"]['+str(sinum)+']/text()').extract()
                            try:
                                t = response.xpath('//tr[@id="v'+str(n)+'"]/td/span[@class="interlinear"]['+str(inum)+']/span/span[@class="interlinear"]['+str(sinum)+']/span[@class="popup"]/span[@lang="en" and position() = last()]/text()').extract()[1]
                                item["Translation"] = re.search(r'\w+(\s[a-z]+)?', t).group()
                            except:
                                pass
                            item["Word"] = anum
                            anum += 1
                            sinum += 1
                            yield item
                        except:
                            pass
                except:
                    pass

                item["Translation"] = " "
                item["Original"] = " "

                if w!=" ":
                    item["Translation"] = " "
                    item["Original"] = w
                    item["Word"] = anum
                    yield item
                    anum += 1

            vs = len(words)+1+len([w for w in words if w!=" "])
            if anum<=vs:
                try:
                    item["Original"] = response.xpath('//tr[@id="v'+str(n)+'"]/td/span[@class="interlinear"]['+str(inum)+']/span/text()').extract()
                    try:
                        t = response.xpath('//tr[@id="v'+str(n)+'"]/td/span[@class="interlinear"]['+str(inum)+']/span/span[@class="popup"]/span[@lang="en" and position() = last()]/text()').extract()[1]
                        item["Translation"] = re.search(r'\w+(\s[a-z]+)?', t).group()
                    except:
                        pass
                    item["Word"] = anum
                    yield item
                except:
                    pass

        base = 'http://en.katabiblon.com/us/'
        url = response.xpath('//a[@class="next-arrow"]/@href')[0].extract()
        yield scrapy.Request(base+url, callback=self.parse)


    """
