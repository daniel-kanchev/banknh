BOT_NAME = 'banknh'
SPIDER_MODULES = ['banknh.spiders']
NEWSPIDER_MODULE = 'banknh.spiders'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
ITEM_PIPELINES = {
    'banknh.pipelines.DatabasePipeline': 300,
}
FEED_EXPORT_ENCODING = 'utf-8'
ROBOTSTXT_OBEY = True

LOG_LEVEL = 'WARNING'

# LOG_LEVEL = 'DEBUG'
