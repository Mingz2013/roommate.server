# coding: utf-8
__author__ = 'zhaojm'

import os
import pymongo
import datetime
# from bson import ObjectId

MONGODB_HOST = os.getenv("MONGODB_HOST", '127.0.0.1')
MONGODB_PORT = os.getenv("MONGODB_PORT", 27017)
mongodb_client_db = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT).sport99


class UserDB(object):

    def __init__(self):
        pass

    @staticmethod
    def add_user(user):
        mongodb_client_db.users.insert(user)

    @staticmethod
    def remove_user_by_id(user_id):
        mongodb_client_db.update({"id": user_id}, {"$set": {"status": 0}})

    @staticmethod
    def get_user_by_id(user_id):
        return mongodb_client_db.users.findOne({"id": user_id})


class BillDB(object):

    def __init__(self):
        pass

    @staticmethod
    def add_bill(bill):
        mongodb_client_db.bills.insert(bill)

    @staticmethod
    def update_bill(bill):
        mongodb_client_db.bills.update({"id": bill.id}, {"$set": bill})

    @staticmethod
    def remove_bill_by_id(bill_id):
        mongodb_client_db.update({"id": bill_id}, {"$set": {"status": 0}})

    @staticmethod
    def get_bill_by_id(bill_id):
        return mongodb_client_db.bills.findOne({"id": bill_id})

    @staticmethod
    def get_all_bills():
        return mongodb_client_db.find({"status": 0})

    @staticmethod
    def get_bills_by_spend_user_id(user_id):
        return mongodb_client_db.bills.find({"spend_user_id": user_id})

    @staticmethod
    def get_bills_by_record_user_id(user_id):
        return mongodb_client_db.bills.find({"record_user_id": user_id})


