#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bsoup
import re
import os


# Build tree of
def build_tree(start, end, path):
    # Искать ссылки можно как угодно, не обязательно через re
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")
    # Словарь вида {"filename1": None, "filename2": None, ...}
    files = dict.fromkeys(os.listdir(path), False)
    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
    queue = [start]
    while queue:
        new_queue = []
        for name in queue:
            with open("{}{}".format(path, name), 'r', encoding='utf-8') as file:
                links = re.findall(link_re, file.read())
            for link in links:
                if files.get(link) is False:
                    files[link] = name
                    if link == end:
                        return files
                    new_queue.append(link)
        queue = new_queue


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    current, bridge = end, [end]
    while current != start:
        current = files[current]
        bridge.append(current)
    return bridge


def get_imgs_count_by_width(body, width):
    """Return (img) with width more than 200. """
    return len(body.find_all('img', width=lambda x: int(x or 0) >= width))


def get_headers_with_chars(body, chars):
    """Count of headers, with begin chars such as: E, T or C"""
    return sum(
        1 for tag in body.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) if
        tag.get_text()[0] in chars)


def get_max_links_len(body):
    """Length of max sequence of links, without duplicate tags between links"""
    tag, max_len = body.find_next('a'), 0
    while tag:
        cur_len = 1
        for tag in tag.find_next_siblings():
            if tag.name != 'a':
                break
            cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
        tag = tag.find_next("a")

    return max_len


def get_count_not_nested_lists(body):
    """Count of list, not nested in other lists"""
    return sum(1 for tag in body.find_all(['ol', 'ul'])
               if not tag.find_parent(['ol', 'ul']))


def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых
    можно добраться от start до end, то, по крайней мере, известны сами start
    и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за
    тест, в этом случае, будет сильно снижена, но на минимальный проходной
    балл наберется, и тест будет пройден. Чтобы получить максимальный балл,
    придется искать все страницы. Удачи!
    """

    # Искать список страниц можно как угодно, даже так: bridge = [end, start]
    bridge = build_bridge(start, end, path)

    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file), 'r', encoding='utf-8') as data:
            soup = bsoup(data, "lxml")
            body = soup.find(id="bodyContent")
            # TODO посчитать реальные значения
            imgs = get_imgs_count_by_width(body, 200)
            headers = get_headers_with_chars(body, "ETC")
            linkslen = get_max_links_len(body)
            lists = get_count_not_nested_lists(body)

            out[file] = [imgs, headers, linkslen, lists]

    return out
