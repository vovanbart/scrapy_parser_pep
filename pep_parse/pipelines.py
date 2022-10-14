import csv
from collections import Counter
from datetime import datetime as dt

from settings import BASE_DIR, RESULT_DIR, TIME_FORMAT, FILE_NAME


class PepParsePipeline:

    def __init__(self) -> None:
        self.results_dir = BASE_DIR / RESULT_DIR
        self.results_dir.mkdir(exist_ok=True)
        self.count_status = Counter()

    def open_spider(self, spider):
        time = dt.now().strftime(TIME_FORMAT)
        file_path = self.results_dir / FILE_NAME.format(time)
        self.file = csv.writer(open(file_path, 'w'))
        self.file.writerow(['Статус', 'Количество'])
        self.file.close()

    def process_item(self, item, spider):
        self.count_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.count_status['Total'] = sum(self.count_status.values())
        self.file.writerows(self.count_status.items())
