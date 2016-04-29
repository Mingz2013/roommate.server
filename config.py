# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 每次请求结束后都会自动提交数据库中的变动
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') \
                               or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') \
    #                        or 'mysql://ydtest:yundong99123@123.206.49.23/test'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') \
                              or 'sqlite:///' + os.path.join(basedir,'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
                              or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config_dict = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}