"""Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]

"""
res = []
with open('nginx_logs.txt','r', encoding='utf-8') as fl:
    fl.seek(0)
    for part in fl:
         prt = part.split()
         res.append((prt[0], prt[5].strip('"'), prt[6]))
for h in res:
       print(h,end='\n')
