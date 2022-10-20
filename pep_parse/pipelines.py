import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR, RESULT_DIR


class PepParsePipeline:
    pep_status_count = defaultdict(int)
    total_pep_count = 0

    def open_spider(self, spider):
        RESULT_DIR.mkdir(exist_ok=True)

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

        output_csv = [('Cтатус', 'Количество')]
        output_csv.extend(self.pep_status_count.items())
        output_csv.append(('Total: ', self.total_pep_count))

        with open(file_path, mode='w', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(output_csv)
