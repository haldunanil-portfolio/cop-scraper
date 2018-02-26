# -*- coding: utf-8 -*-
import scrapy


class LawEnforcementAgencySpider(scrapy.Spider):
    name = 'agencies'
    allowed_domains = ['policeone.com']
    start_urls = ['https://www.policeone.com/law-enforcement-directory/page-%s/' % i for i in range(1, 477)]

    def parse(self, response):
        results = response.xpath("//div[@id='search-results']")
        agencies = results.css('tr')

        for agency in agencies:
            data = agency.css('td.odd') + agency.css('td.even')

            # skip empty lists
            if len(data) > 0:
                href = data[0].css('a::attr(href)').extract_first()

                yield response.follow(href, self.parse_details)

    def parse_details(self, response):
        def helper(items):
            keys = items.css('b::text').extract()
            values = items.css('p::text').extract()

            return {
                key.split(':')[0].strip(): value.strip()
                for key, value in zip(keys, values)
            }

        info = response.css('div.dep-block-info')

        contact_info = helper(info[0])
        addtl_info = helper(info[1])

        yield {**contact_info, **addtl_info}