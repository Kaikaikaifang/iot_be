# python
# -*- coding: UTF-8 -*-
"""
@Project ：A-login-demo 
@File    ：config.py
@Author  ：kaikai
@Date    ：2022/10/21 23:13 
"""
import os
from .code import code

basedir = os.path.abspath(os.path.dirname(__file__))  # 获得当前文件的绝对路径


class Config:
    """基类: 通用配置"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a nice key'  # 可以在生产环境中设置密钥, 'a nice key' 是默认密钥, 在开发环境中使用
    CODE = code

    @staticmethod
    def init_app(app):
        """为flask实例提供的修改配置的接口"""
        pass


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    MONGO_URI = os.environ.get('DEV_DATABASE_URL') or "mongodb://localhost:27017/A-login-demo-dev"


class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True
    MONGO_URI = os.environ.get('TEST_DATABASE_URL') or "mongodb://localhost:27017/test"


class ProductionConfig(Config):
    """生产环境配置"""
    MONGO_URI = os.environ.get('DATABASE_URL') or "mongodb://localhost:27017/A-login-demo"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    # 默认配置: 生产环境配置
    'default': ProductionConfig
}