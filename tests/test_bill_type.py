# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


from commons import get, post, put, delete


def test_index():
    url = 'http://127.0.0.1:5000/bill_type'
    get(url)
    pass


def test_post():
    url = 'http://127.0.0.1:5000/bill_type/post'
    payload = {'id': 1, 'name': ''}
    post(url, payload)
    pass


def test_list():
    url = 'http://127.0.0.1:5000/bill_type/list'
    get(url)
    pass


def test_detail():
    url = 'http://127.0.0.1:5000/bill_type/detail/1'
    get(url)
    pass


def test_update():
    url = 'http://127.0.0.1:5000/bill/update'
    payload = {'id': 1, 'name': ''}
    put(url, payload)
    pass


def test_delete():
    url = 'http://127.0.0.1:5000/bill_type/delete/1'
    delete(url)
    pass


if __name__ == '__main__':
    test_index()
    pass
