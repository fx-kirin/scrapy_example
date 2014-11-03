# -*- coding: utf-8 -*-

BOT_NAME = 'scrapy_example'

SPIDER_MODULES = ['scrapy_example.spiders']
NEWSPIDER_MODULE = 'scrapy_example.spiders'

# ダウンロードする間隔（秒）の指定
DOWNLOAD_DELAY = 3

# pipelineの設定
ITEM_PIPELINES = ['scrapy_example.pipelines.JsonWithEncodingPipeline']
