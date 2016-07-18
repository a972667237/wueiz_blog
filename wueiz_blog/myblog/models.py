from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField('标题',max_length=200)
    content = models.TextField('内容',max_length=1000)
    date = models.DateField('日期')
    author = models.ManyToManyField('author')
    tag = models.ManyToManyField('tag')
    recommond = models.BooleanField('推荐',default=False)
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date']
    def __str__(self):
        return self.title

class author(models.Model):
    name = models.CharField('作者名',max_length=10)
    email = models.EmailField('邮箱')
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class tag(models.Model):
    name = models.CharField('标签名',max_length=10)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name