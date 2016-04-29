# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from app import db
from app.models import User, Bill, BillType


class UserDB(object):

    def __init__(self):
        pass

    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def remove_user_by_id(id):
        user = db.session.query(User).filter(User.id == id, User.status == 0).first()
        if user:
            user.status = -1
            db.session.add(user)
            db.session.commit()
        else:
            raise Exception("user not found")

    @staticmethod
    def get_user_by_id(id):
        return db.session.query(User).filter(User.id == id, User.status == 0).first()

    @staticmethod
    def get_all_users():
        return db.session.query(User).filter(User.status == 0).all()

    @staticmethod
    def update_user(user):
        db.session.add(user)
        db.session.commit()


class BillDB(object):

    def __init__(self):
        pass

    @staticmethod
    def add_bill(bill):
        db.session.add(bill)
        db.session.commit()

    @staticmethod
    def update_bill(bill):
        db.session.add(bill)
        db.session.commit()

    @staticmethod
    def remove_bill_by_id(id):
        bill = db.session.query(Bill).filter(Bill.id == id, Bill.status == 0).first()
        if bill:
            bill.status = -1
            db.session.add(bill)
            db.session.commit()
        else:
            raise Exception("bill not found")

    @staticmethod
    def get_bill_by_id(id):
        return db.session.query(Bill).filter(Bill.id == id, Bill.status == 0).first()

    @staticmethod
    def get_all_bills():
        return db.session.query(Bill).filter(Bill.status == 0).all()

    @staticmethod
    def get_bills_by_spend_user_id(user_id):
        return db.session.query(Bill).filter(Bill.spend_user_id == user_id, Bill.status == 0).all()

    @staticmethod
    def get_bills_by_record_user_id(user_id):
        return db.session.query(Bill).filter(Bill.record_user_id == user_id, Bill.status == 0).all()


class BillTypeDB(object):

    def __init__(self):
        pass

    @staticmethod
    def add_bill_type(bill_type):
        db.session.add(bill_type)
        db.session.commit()

    @staticmethod
    def update_bill_type(bill_type):
        db.session.add(bill_type)
        db.session.commit()

    @staticmethod
    def remove_bill_type_by_id(id):
        bill_type = db.session.query(BillType).filter(BillType.id == id, BillType.status == 0).first()
        if bill_type:
            bill_type.status = -1
            db.session.add(bill_type)
            db.session.commit()
        else:
            raise Exception("bill type not found")

    @staticmethod
    def get_bill_type_by_id(id):
        return db.session.query(BillType).filter(BillType.id == id, BillType.status == 0).first()

    @staticmethod
    def get_all_bill_types():
        return db.session.query(BillType).filter(BillType.status == 0).all()


