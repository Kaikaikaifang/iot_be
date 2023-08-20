# python
# -*- coding: UTF-8 -*-
"""
@Project ：A-login-demo 
@File    ：__init__.py
@Author  ：kaikai
@Date    ：2022/10/21 23:48 
"""
from flask import Flask, current_app
# from flask_pymongo import PyMongo
from .config import config
from flask_cors import CORS
from flask_socketio import SocketIO


cors = CORS()
allow_origin = ['http://localhost:5000', 'http://electrocardiogram-1310574317.cos-website.ap-nanjing.myqcloud.com']

"""伪初始化扩展: 目的是向外暴露扩展实例"""
# mongo = PyMongo()
socketio = SocketIO()


def create_app(config_name='default'):
    """
    工厂函数: 用于创建Flask应用实例
    :param config_name: 配置名称 enu: ['default', 'production', 'testing', 'development']  default: 'default'
    """
    # 1. 创建应用实例并初始化配置
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 向应用实例导入配置对象
    config[config_name].init_app(app)  # 可以定制初始化配置接口来进行更为复杂的初始化配置操作, 现在还没啥用, 上面那行就够用了

    # 2. 初始化扩展
    # mongo.init_app(app)
    cors.init_app(app, resources={r"/*": {"origins": allow_origin}})
    socketio.init_app(app, cors_allowed_origins='*')

    # 3. 注册蓝本到应用实例上
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix="/")

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")
    return app, socketio


