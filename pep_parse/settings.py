from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

FEED_URI_PARAMS = 'pep_parse.utils.uri_params'
BASE_DIR = Path(__file__).parents[1]
RESULT_DIR = 'results'
TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_NAME = 'status_summary_{}.csv'
