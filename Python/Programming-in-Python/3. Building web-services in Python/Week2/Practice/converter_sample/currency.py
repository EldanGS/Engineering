from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    # Использовать переданный requests
    response = requests.get(f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}")
    soup = BeautifulSoup(response.content, 'xml')
    cur = {}
    for val in [cur_from, cur_to]:
        if val == 'RUR':
            cur[val] = {'nominal': Decimal(1), 'value': Decimal(1)}
        else:
            item = soup.find('CharCode', text=val).parent
            cur[val] = {'nominal': Decimal(item.Nominal.text),
                        'value': Decimal(item.Value.text.replace(',', '.'))}

    result = (amount * cur[cur_from]['value'] / cur[cur_from]['nominal']
              / cur[cur_to]['value'] * cur[cur_to]['nominal'])
    # не забыть про округление до 4х знаков после запятой
    return result.quantize(Decimal('.0001'))

# convert(1, 'JPY', 'RUR', "17/02/2005", requests)
#
