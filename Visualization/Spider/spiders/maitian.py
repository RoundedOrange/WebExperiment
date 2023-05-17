import math
import re
count = 1
import scrapy
from Spider.items import SpiderItem
class MaitianSpider(scrapy.Spider):
    name = "maitian"
    allowed_domains = ["xm.maitian.cn"]
    start_urls = ['http://xm.maitian.cn/zfall/PG1']

    def parse(self, response):
        global count
        count += 1
        house_list = response.xpath('//div[@class="list_wrap"]/ul/li')
        for li in house_list:
            try:
                item = SpiderItem()
                item['price'] = li.xpath('./div[@class="list_title"]/div[@class="the_price"]/ol/strong/span/text()').extract_first()
                item['title'] = li.xpath('./div[@class="list_title"]/h1/a/text()').extract_first().strip()
                item['area'] = li.xpath('./div[@class="list_title"]/p/span/text()').extract()[0][:-1]
                item['bedroom_num'] = 0
                item['hall_num'] = 0
                item['toilet_num'] = 0
                item['balcony_num'] = 0
                for i in range(4):
                    temp = li.xpath('./div[@class="list_title"]/p/span/text()').extract()[i+1][-1]
                    if temp == "室":
                        item['bedroom_num'] = math.floor(float(li.xpath('./div[@class="list_title"]/p/span/text()').extract()[i+1][:-1]))
                    if temp == "厅":
                        item['hall_num'] = math.floor(float(li.xpath('./div[@class="list_title"]/p/span/text()').extract()[i+1][:-1]))
                    if temp == "卫":
                        item['toilet_num'] = math.floor(float(li.xpath('./div[@class="list_title"]/p/span/text()').extract()[i+1][:-1]))
                    if temp == "阳":
                        item['balcony_num'] = math.floor(float(li.xpath('./div[@class="list_title"]/p/span/text()').extract()[i+1][:-1]))
                item['usage'] = li.xpath('./div[@class="list_title"]/p/span/text()').extract()[-8]
                item['renting_type'] = '整租' if (
                        li.xpath('./div[@class="list_title"]/p/span/text()').extract()[-7] == '整租') else '合租'
                item['floor_height'] = li.xpath('./div[@class="list_title"]/p/span/text()').extract()[-6][0]
                item['floor'] = li.xpath('./div[@class="list_title"]/p/span/text()').extract()[-5][:-1]
                item['has_elevator'] = True if (li.xpath('./div[@class="list_title"]/p/span/text()').extract()[-4][0] == '有') else False
                item['facing'] = li.xpath('./div[@class="list_title"]/p/span/text()').extract()[-3]
                item['address'] = li.xpath('./div[@class="list_title"]/p[@class="house_hot"]/span/text()').extract()[0].strip()
                item['location'] = re.sub('\s',' ',li.xpath('./div[@class="list_title"]/p[@class="house_hot"]/span/text()').extract()[1]).strip()
                item['tags'] = []
                for tag in li.xpath(
                        './div[@class="list_title"]/dl[@class="clearfix"]/dd[@class="morel clearfix"]/label/text()').extract():
                    item['tags'].append(tag)
                yield item
            except BaseException:
                print("出错啦！")
                continue

        next_url = 'http://xm.maitian.cn/zfall/PG' + str(count)
        if count <= 100:
            yield scrapy.Request(next_url)