# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, request, jsonify, current_app

from app.dbs.sqlalchemy import BillDB, UserDB
from ..models import Bill
from ..utils import require_value_from_dict, model2dict

api = Blueprint('bill_controller', __name__, url_prefix='/bill')


@api.route('/', methods=['GET'])
def index():
    return 'bill index'


@api.route('/post', methods=['POST'])
def post():
    try:
        bill = Bill(request.form)
        BillDB.add_bill(bill)
        return jsonify({"code": 0})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/list', methods=['GET'])
def bill_list():
    try:
        bills = BillDB.get_all_bills()
        bills_copy = []
        for bill in bills:
            bills_copy.append(model2dict(bill))
        return jsonify({"code": 0, "result": bills_copy})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/list/<int:user_id>', methods=['GET'])
def bill_list_by_spend_user_id(user_id):
    try:
        user = UserDB.get_user_by_id(user_id)
        if not user:
            return jsonify({"code": -1, "error": "user not found"})
        bills = BillDB.get_bills_by_spend_user_id(user_id)
        bills_copy = []
        for bill in bills:
            bills_copy.append(model2dict(bill))
        return jsonify({"code": 0, "result": bills_copy})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/detail/<int:id>', methods=['GET'])
def detail(id):
    try:
        bill = BillDB.get_bill_by_id(id)
        return jsonify({"code": 0, "result": model2dict(bill)})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/update', methods=['PUT'])
def update():
    try:
        id = require_value_from_dict(request.form, "id")
        bill = BillDB.get_bill_by_id(id)
        if not bill:
            return jsonify({"code": -1, "error": "bill not found"})
        bill.update_from_json(request.form)
        BillDB.update_bill(bill)
        return jsonify({"code": 0})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        BillDB.remove_bill_by_id(id)
        return jsonify({"code": 0})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


