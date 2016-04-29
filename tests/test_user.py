# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from commons import get, post, put, delete


def test_index():
    url = 'http://127.0.0.1:5000/user'
    get(url)
    pass


def test_post():
    url = 'http://127.0.0.1:5000/user/post'
    payload = {'name': '陆杰', 'nick': 'lj', 'email': '305603665@qq.com',
               'mobile': '15901487291', 'password': 'my pass'}
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
    payload = {'id': 1, 'name': '赵景明', 'nick': '明子', 'email': '305603665@qq.com',
               'mobile': '15901487291', 'password': 'my pass'}
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
