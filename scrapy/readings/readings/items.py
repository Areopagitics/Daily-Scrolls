
''''

from scrapy.item import Item, Field

class ReadingsItem(Item):
    day = Field()
    week = Field()
    date = Field()
    first_reading = Field()
    psalm = Field()
    second_reading = Field()
    alleluia = Field()
    gospel = Field()
'''