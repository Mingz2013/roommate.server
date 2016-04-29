# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app import db
from utils import require_value_from_dict, get_value_from_dict


class BillType(db.Model):
    __tablename__ = 'bill_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))

    status = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name
        self.status = 0
        pass

    def __repr__(self):
        return '<BillType %r>' % self.name

    def update_from_json(self, arr):
        self.name = require_value_from_dict(arr, "name")
        self.status = 0
        pass

    def to_json(self):
        json_bill_type = {
            "id": self.id,
            "name": self.name,
            "status": self.status,
        }
        return json_bill_type


class Bill(db.Model):
    __tablename__ = 'bills'
    id = db.Column(db.Integer, primary_key=True)
    record_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)   # 记录者
    spend_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)   # 消费者
    type_id = db.Column(db.Integer, db.ForeignKey("bill_types.id"), index=True)
    desc = db.Column(db.String(30))     # 说明
    money = db.Column(db.Float)
    date = db.Column(db.Date)

    status = db.Column(db.Integer)  # 0: 正常, -1: 删除

    def __init__(self, arr):
        self.record_user_id = require_value_from_dict(arr, "record_user_id")
        self.spend_user_id = require_value_from_dict(arr, "spend_user_id")
        self.type_id = require_value_from_dict(arr, "type_id")
        self.desc = require_value_from_dict(arr, "desc")
        self.money = require_value_from_dict(arr, 'money')
        self.date = require_value_from_dict(arr, "date")
        self.status = 0
        pass

    def __repr__(self):
        return '<Bill %r>' % self.name

    def update_from_json(self, arr):
        self.record_user_id = require_value_from_dict(arr, "record_user_id")
        self.spend_user_id = require_value_from_dict(arr, "spend_user_id")
        self.type_id = require_value_from_dict(arr, "type_id")
        self.desc = require_value_from_dict(arr, "desc")
        self.money = require_value_from_dict(arr, 'money')
        self.date = require_value_from_dict(arr, "date")
        self.status = 0
        pass

    def to_json(self):
        json_bill = {
            "id": self.id,
            "record_user_id": self.record_user_id,
            "spend_user_id": self.spend_user_id,
            "type_id": self.type_id,
            "desc": self.desc,
            "money": self.money,
            "date": self.date,
            "status": self.status,
        }
        return json_bill

    # @staticmethod
    # def from_json(json_bill):
    #     # 验证字段，并
    #     pass


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(10))
    password = db.Column(db.String(20))
    name = db.Column(db.String(10))
    mobile = db.Column(db.String(11))
    email = db.Column(db.String(30))

    status = db.Column(db.Integer)  # 0: 正常, -1: 删除

    def __init__(self, arr):
        self.nick = require_value_from_dict(arr, "nick")
        self.password = require_value_from_dict(arr, "password")
        self.name = require_value_from_dict(arr, "name")
        self.mobile = require_value_from_dict(arr, "mobile")
        self.email = require_value_from_dict(arr, "email")
        self.status = 0
        pass

    def __repr__(self):
        return '<User name:= %r, nick:= %r>' % (self.name, self.nick)

    def update_from_json(self, arr):
        self.nick = require_value_from_dict(arr, "nick")
        self.password = require_value_from_dict(arr, "password")
        self.name = require_value_from_dict(arr, "name")
        self.mobile = require_value_from_dict(arr, "mobile")
        self.email = require_value_from_dict(arr, "email")
        self.status = 0

    def to_json(self):
        json_user = {
            "id": self.id,
            "nick": self.nick,
            "password": self.password,
            "name": self.name,
            "mobile": self.mobile,
            "email": self.email,
            "status": self.status,
        }
        return json_user

