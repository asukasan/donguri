from django.db import models
from datetime import datetime



class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name='タイトル', blank=True, null=False)
    created_at = models.DateTimeField(default=datetime.now, verbose_name='作成時間')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新時間')
    heading = models.CharField(verbose_name='見出し', blank=True, null=True, max_length=200)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    view_count = models.IntegerField(verbose_name='閲覧人数', blank=True, null=True, default=0)
    thumbnail = models.ImageField(verbose_name='サムネイル', null=True, blank=True)
    is_public = models.BooleanField(default=True, verbose_name='公開可能か')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='カテゴリ', null=True, blank=True)
    recommendation = models.ManyToManyField("self", verbose_name='おすすめ',blank=True)
    group = models.ForeignKey("Group", on_delete=models.CASCADE, verbose_name='グループ', null=True, blank=True)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='名前')

    def __str__(self):
        return self.name        

class Group(models.Model):
    name = models.CharField(max_length=64, verbose_name='名前')
    
    def __str__(self):
        return self.name
