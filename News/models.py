from SmartDjango import models, E, Hc


@E.register(id_processor=E.idp_cls_prefix())
class NewsError:
    GET = E('News not found', hc=Hc.NotFound)


class News(models.Model):
    title = models.TextField()

    abstract = models.TextField()

    category = models.CharField(
        max_length=128,
    )

    subcategory = models.CharField(
        max_length=128,
    )

    nid = models.CharField(
        max_length=10,
        unique=True,
        db_index=True,
    )

    body = models.TextField(default=None, null=True)

    @classmethod
    def get(cls, nid):
        try:
            return cls.objects.get(nid=nid)
        except Exception:
            raise NewsError.GET

    @classmethod
    def create(cls, nid, **kwargs):
        try:
            return cls.get(nid=nid)
        except:
            return cls.objects.create(nid=nid, **kwargs)

    def d_base(self):
        return self.dictify('title', 'abstract', 'category', 'subcategory', 'nid')

    def d(self):
        d_ = self.d_base()
        d_.update(
            body=self.body,
            recommend=Recommend.get_recommend(self).dict(lambda recommend: News.d_base(recommend.target))
        )
        return d_


class Recommend(models.Model):
    source = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='source'
    )

    target = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='target'
    )

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def get_recommend(cls, source):
        return cls.objects.filter(source=source)


class NewsP:
    nid = News.get_param('nid')
    nid_getter = nid.rename('nid', yield_name='news').process(News.get)
