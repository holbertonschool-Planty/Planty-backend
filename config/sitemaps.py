from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class APISitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return ['api:docs']

    def location(self, item):
        return f'/api/docs/'
