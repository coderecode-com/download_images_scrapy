

BOT_NAME = 'download_images'

SPIDER_MODULES = ['download_images.spiders']
NEWSPIDER_MODULE = 'download_images.spiders'
FEED_EXPORT_FIELDS =["title","price"]
ITEM_PIPELINES = {
   'download_images.pipelines.CustomImagesPipeline': 1,
}
IMAGES_STORE='product_images'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
