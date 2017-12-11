'''MSS: Instagram Spider'''
import json

from scrapy import Spider


class Instagram(Spider):
    '''MSS: Instagram Spider'''
    name = 'Instagram'
    start_urls = [
        'https://www.instagram.com/onionman__/',
    ]

    def parse(self, response):
        '''Parse profile JSON data'''
        json_string = response.xpath('//script/text()').re(r'sharedData = (.+);')[0]
        self.saveJson(json.loads(json_string))
        return json.loads(json_string)
    
    def saveJson(self, jsonStr):
        with open ('../data/instagram.json','w') as f:
            json.dump(jsonStr,f)
