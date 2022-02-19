import requests

def currency_rates(main_value):
    responce = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    counts = responce.text
    exit = None
    if main_value not in counts:
        return exit
    else:
        for numb in counts.split(f'{main_value}')[1:]:
            for numb1 in numb.split('</Value>')[:1]:
                exit = round(float(numb1.split('<Value>')[1].replace(',','.')),4)
                return exit
