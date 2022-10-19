from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    pep_status_count = defaultdict(int)
    total_pep_count = 0

    def open_spider(self, spider):
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        if item.get('status'):
            self.total_pep_count += 1
            self.pep_status_count[
                item['status']] = self.pep_status_count.get(
                item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{now}.csv'
        file_path = BASE_DIR / 'results' / file_name
        with open(file_path, mode='w', encoding='utf-8') as file:
            file.write('Статус,Количество\n')
            for status in self.pep_status_count:
                file.write(f'{status},{self.pep_status_count[status]}\n')
            file.write(f'Total,{self.total_pep_count}\n')
