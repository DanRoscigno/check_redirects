from scrapy.spiders import SitemapSpider


class RedirectsSpider(SitemapSpider):
    name = "redirects"
    allowed_domains = ["www.starrocks.io"]
    sitemap_urls = ["https://www.starrocks.io/sitemap.xml"]

    def parse(self, response):
        pass
