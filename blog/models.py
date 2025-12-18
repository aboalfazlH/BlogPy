from django.db import models

"""
وقت مایگریشن نیست!
"""
class Blog(models.Model):
    name = models.CharField(verbose_name="نام وبلاگ",max_length=110)
    description = models.TextField(verbose_name="توضیحات وبلاگ",blank=True,null=True)
    anonymons_bloger = models.BooleanField(verbose_name="ناشناس کردن نویسنده",default=False,help_text="اگر فعال شود نام نویسنده در بلاگ نمایش داده نمی شود")
    
    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(verbose_name="موضوع")
    description = models.TextField(verbose_name="توضیحات",blank=True,null=True)