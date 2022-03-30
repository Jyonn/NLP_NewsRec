import random

from SmartDjango import Analyse
from django.views import View

from News.models import News, NewsP


class HomeView(View):
    @staticmethod
    def get(_):
        all_news = News.objects.all()
        news_indexes = list(range(News.objects.count()))
        random.shuffle(news_indexes)
        return [all_news[index].d_base() for index in news_indexes[:10]]


class NewsView(View):
    @staticmethod
    @Analyse.r(a=[NewsP.nid_getter])
    def get(r):
        news = r.d.news
        return news.d()
