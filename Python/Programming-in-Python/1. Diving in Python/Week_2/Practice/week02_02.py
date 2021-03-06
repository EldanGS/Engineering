#!/bin/python3
# -*- coding: utf-8 -*-

"""
Programming Assignment: Декоратор to_json

Чтобы передавать данные между функциями, модулями или разными системами используются форматы данных. 
Одним из самых популярных форматов является JSON. Напишите декоратор to_json, 
который можно применить к различным функциям, чтобы преобразовывать их возвращаемое значение в JSON-формат. 
Не забудьте про сохранение корректного имени декорируемой функции.
"""

import json
from functools import wraps

# https://docs.python.org/3/library/functools.html#functools.wraps
def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return wrapper

# @to_json
# def get_data():
#   return {
#     'data': 42
#   }
  
# get_data()