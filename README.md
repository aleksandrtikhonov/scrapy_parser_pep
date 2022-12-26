# «Scrapy_parser_pep - асинхронный парсер PEP» 
___
### **_Парсер [документов PEP](https://www.python.org/dev/peps/) на базе фреймворка Scrapy._**
___

## Установка и запуск
1. Клонировать репозиторий:

```bash
git clone https://github.com/aleksandrtikhonov/bs4_parser_pep.git
```
2. Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
source venv/bin/activate
```
3. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
___

## Запуск парсера:
```
scrapy crawl pep
```
___
## Результаты работы парсера:
Парсер выводит собранную информацию в два csv файла в каталог`results/`:
- `pep_%date+time%.csv` - список всех PEP: номер, название и статус.
  

- `status_summary_%date+time%.csv` содержится сводка по статусам PEP — 
  агрегированные данные по каждому статусу и общее количество всех документов.
  
___

## Автор:
Александр Тихонов, студент курса "Python Разработчик+"
