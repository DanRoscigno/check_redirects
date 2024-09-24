from scrapy.spiders import SitemapSpider


class RedirectsSpider(SitemapSpider):
    handle_httpstatus_all = True
    name = "redirects"
    allowed_domains = ["starrocks.io"]
    sitemap_urls = ["https://www.starrocks.io/sitemap.xml"]

    sitemapLinks = []
    pageLinks = []

    def parse(self, response):
        self.sitemapLinks.append(response.url)
        for href in response.css('a::attr(href)'):
            self.pageLinks.append(response.url)
        for link in self.pageLinks:
            if link is not None:
                if not link.startswith("https://starrocks.io/"):
                    page_url = ("https://starrocks.io/" + link)
                next_page = response.urljoin(link)
                # yield scrapy.Request(next_page, callback=self.parse)
                yield response.follow(next_page, callback=self.checkonly)

    def checkonly(self, response):
        self.logger.info("got response for %r" % response.url)

