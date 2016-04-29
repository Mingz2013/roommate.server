# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, render_template
api = Blueprint('index_controller', __name__, url_prefix='/')


@api.route('/', methods=['GET'])
def index():
    return "test index"
    # return render_template('index/index.html')

