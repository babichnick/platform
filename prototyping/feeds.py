from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import DefaultFeed
from django.urls import reverse
from prototyping.models import Link

class CorrectMimeTypeFeed(DefaultFeed):
    content_type = 'application/xml; charset=utf-8'

class LatestNewsFeed(Feed):
    feed_type = CorrectMimeTypeFeed
    title = "UX design digest"
    link = "/feed/"
    description = "Popular news for UX designers"

    def items(self):
        return Link.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.tease