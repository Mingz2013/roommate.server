# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from commons import get, post, put, delete


def test_index():
    url = 'http://127.0.0.1:5000/user'
    get(url)
    pass


def test_post():
    url = 'http://127.0.0.1:5000/user/post'
    payload = {'name': 'lj', 'nick': 'lj', 'email': '111111@qq.com',
               'mobile': '11111111111', 'password': 'my pass'}
    post(url, payload)
    pass


def test_list():
    url = 'http://127.0.0.1:5000/user/list'
    get(url)
    pass


def test_detail():
    url = 'http://127.0.0.1:5000/user/detail/1'
    get(url)
    pass


def test_update():
    url = 'http://127.0.0.1:5000/user/update'
    payload = {'id': 1, 'name': 'mz', 'nick': 'mz', 'email': '111111@qq.com',
               'mobile': '11111111111', 'password': 'my pass'}
    put(url, payload)
    pass


def test_delete():
    url = 'http://127.0.0.1:5000/user/delete/1'
    delete(url)
    pass


if __name__ == '__main__':
    # test_index()
    # test_post()
    # test_list()
    # test_update()
    # test_detail()
    test_delete()
    pass
