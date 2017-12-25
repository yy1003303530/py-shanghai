from rest_framework import serializers
from .models import *
class PageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id','title','content','slug','category_id','is_valid','create_time','update_time')


class PageCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = PageCategory
        fields =('id','page_category_name','parent_id')
