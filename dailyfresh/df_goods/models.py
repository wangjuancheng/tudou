from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20,verbose_name='分类')
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20,help_text='标题',verbose_name='标题')
    gpic = models.ImageField(upload_to='df_goods/',verbose_name='上传图片')
    gprice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='价格')
    isDelete = models.BooleanField(default=20)
    gunit = models.CharField(max_length=20,default='500g',verbose_name='份量')
    gclick = models.IntegerField(verbose_name='点击量')
    gbrief = models.CharField(max_length=200,verbose_name='简介')
    gkuncun = models.IntegerField(verbose_name='库存')
    gcontent = HTMLField(verbose_name='介绍')
    gtype = models.ForeignKey(TypeInfo,on_delete=models.CASCADE)
    # gadv = models.BooleanField(default=False)