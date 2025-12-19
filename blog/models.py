from django.db import models

class Blog(models.Model):
    name = models.CharField(verbose_name="نام وبلاگ",max_length=110)
    description = models.TextField(verbose_name="توضیحات وبلاگ",blank=True,null=True)
    anonymos_bloger = models.BooleanField(verbose_name="ناشناس کردن نویسنده",default=False,help_text="اگر فعال شود نام نویسنده در بلاگ نمایش داده نمی شود")
    bloger = models.ForeignKey("accounts.CustomUser",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "وبلاگ"    
        verbose_name_plural = "وبلاگ ها"    

class Article(models.Model):
    title = models.CharField(verbose_name="موضوع")
    summary = models.TextField(verbose_name="خلاصه")
    description = models.TextField(verbose_name="توضیحات",blank=True,null=True)
    slug = models.SlugField(verbose_name="شناسه")
    thumbnail = models.ImageField("تصویر بندانگشتی",unique=True)
    author = models.ForeignKey("accounts.CustomUser",on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name="فعال",default=True)
    is_verify = models.BooleanField(verbose_name="مورد تائید",default=True)
    is_pin = models.BooleanField(verbose_name="ویژه",default=False)

    class Meta:
        verbose_name = "مقاله"    
        verbose_name_plural = "مقالات"    

    def __str__(self):
        return self.title
