# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import requests


def post(url, payload):
    r = requests.post(url, data=payload)
    print(r.text)


def get(url):
    r = requests.get(url)
    print(r.text)


def delete(url):
    r = requests.delete(url)
    print(r.text)


def put(url, payload):
    r = requests.put(url, data=payload)
    print(r.text)