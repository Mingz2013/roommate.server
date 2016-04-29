# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, request, jsonify, current_app

from app.dbs.sqlalchemy import BillTypeDB
from ..models import BillType
from ..utils import require_value_from_dict, model2dict

api = Blueprint('bill_type_controller', __name__, url_prefix='/bill_type')


@api.route('/', methods=['GET'])
def index():
    return 'bill type index'


@api.route('/post', methods=['POST'])
def post():
    try:
        bill_type = BillType(request.form)
        BillTypeDB.add_bill_type(bill_type)
        return jsonify({"code": 0})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/list', methods=['GET'])
def bill_type_list():
    try:
        bill_types = BillTypeDB.get_all_bill_types()
        bill_types_copy = []
        for bill_type in bill_types:
            bill_types_copy.append(model2dict(bill_type))
        return jsonify({"code": 0, "result": bill_types_copy})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/detail/<int:id>', methods=['GET'])
def detail(id):
    try:
        bill_type = BillTypeDB.get_bill_type_by_id(id)
        return jsonify({"code": 0, "result": bill_type})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/update', methods=['PUT'])
def update():
    try:
        id = require_value_from_dict(request.form, "id")
        bill_type = BillTypeDB.get_bill_type_by_id(id)
        if not bill_type:
            return jsonify({"code": -1, "error": "bill type not found"})
        bill_type.update_from_json(request.form)
        BillTypeDB.update_bill_type(bill_type)
        return jsonify({"code": 0})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        BillTypeDB.remove_bill_type_by_id(id)
        return jsonify({"code": 0})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


