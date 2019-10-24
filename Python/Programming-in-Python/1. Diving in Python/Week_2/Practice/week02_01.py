#!/bin/python3
# -*- coding: utf-8 -*-

"""

На этой неделе мы с вами реализуем собственный key-value storage. Вашей задачей будет написать скрипт, который принимает в качестве аргументов ключи и значения и выводит информацию из хранилища (в нашем случае — из файла).

Запись значения по ключу

> storage.py --key key_name --val value

Получение значения по ключу

> storage.py --key key_name

Ответом в данном случае будет вывод с помощью print соответствующего значения

> value

или

> value_1, value_2

если значений по этому ключу было записано несколько. Метрики сохраняйте в порядке их добавления. Обратите внимание на пробел после запятой.

Если значений по ключу не было найдено, выводите пустую строку или None.

Для работы с аргументами командной строки используйте модуль argparse. Вашей задачей будет считать аргументы, переданные вашей программе, и записать соответствующую пару ключ-значение в файл хранилища или вывести значения, если был передан только ключ. Хранить данные вы можете в формате JSON с помощью стандартного модуля json. Проверьте добавление нескольких ключей и разных значений.

Файл следует создавать с помощью модуля tempfile.


import os
import tempfile
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data'
    )
with open(storage_path, 'w') as f:
  ...
Создайте скрипт хранилища и загрузите его на платформу.

"""

import os
import json
import tempfile
import argparse


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def init(storage_path):
	if not os.path.isfile(storage_path) or os.stat(storage_path).st_size == 0:
		return {}

	with open(storage_path, 'r') as file:
		return json.load(file)


def put(key, value):
	data = init(storage_path)

	args.val = [w.replace(',', '') for w in args.val]

	if args.key in data:
		for new_value in args.val:
			data[args.key].append(new_value)
	else:
		data[args.key] = args.val

	with open(storage_path, 'w') as file:
		file.write(json.dumps(data))


def get(key):
	data = init(storage_path)
	return ', '.join(data[args.key]) if args.key in data else None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key', required=True)
    parser.add_argument('--val', help='Value', nargs='+', type=str)
    args = parser.parse_args()

    if args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        print(get(args.key))
    else:
        print('Wrong command')
	


"""
author solution:
import argparse
import json
import os
import tempfile


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def clear():
    os.remove(storage_path)


def get_data():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)

        return {}


def put(key, value):
    data = get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))


def get(key):
    data = get_data()
    return data.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    parser.add_argument('--clear', action='store_true', help='Clear')

    args = parser.parse_args()

    if args.clear:
        clear()
    elif args.key and args.val:
        put(args.key, args.val)
    elif args.key:
        print(get(args.key))
    else:
        print('Wrong command')
        
"""




