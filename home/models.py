from django.db import models

# Create your models here.
class Page(models.Model):
    """内面内容表"""
    # 页面标题
    title = models.CharField(max_length=50)
    # 页面内容
    content = models.TextField(max_length=20000)
    # 页面标记
    slug =  models.CharField(max_length=20)
    # 页面类别id
    category_id = models.IntegerField()
    #是否有效果
    is_valid = models.BooleanField(default=True)
    # 页面创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 页面update时间
    update_time = models.DateTimeField(auto_now=True)
class PageCategory(models.Model):
    """页面类别表"""
    #页面分类名称
    page_category_name = models.CharField(max_length=20)
    # 页面分类父ID
    parent_id = models.IntegerField(default=0)