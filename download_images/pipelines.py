# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class DownloadImagesPipeline:
#     def process_item(self, item, spider):
#         return item
from scrapy.pipelines.images import ImagesPipeline
from slugify import slugify

class CustomImagesPipeline(ImagesPipeline):
    
    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = slugify(item.get('title'),max_length=200)
        return f'full/{image_name}.jpg'