# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, request, jsonify, current_app

from app.dbs.sqlalchemy import UserDB
from ..models import User
from ..utils import require_value_from_dict, model2dict


api = Blueprint('user_controller', __name__, url_prefix='/user')


@api.route('/', methods=['GET'])
def index():
    return 'user index'


@api.route('/post', methods=['POST'])
def post():
    try:
        user = User(request.form)
        UserDB.add_user(user)
        return jsonify({"code": 0})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/list', methods=['GET'])
def user_list():
    try:
        users = UserDB.get_all_users()
        users_copy = []
        for user in users:
            users_copy.append(model2dict(user))
        return jsonify({"code": 0, "result": users_copy})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/detail/<int:id>', methods=['GET'])
def detail(id):
    try:
        user = UserDB.get_user_by_id(id)
        return jsonify({"code": 0, "result": model2dict(user)})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/update', methods=['PUT'])
def update():
    try:
        id = require_value_from_dict(request.form, "id")
        user = UserDB.get_user_by_id(id)
        if not user:
            return jsonify({"code": -1, "error": "user not found"})
        user.update_from_json(request.form)
        print model2dict(user)
        UserDB.update_user(user)
        return jsonify({"code": 0})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})


@api.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        UserDB.remove_user_by_id(id)
        return jsonify({"code": 0})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({"code": -1, "error": e.message})

