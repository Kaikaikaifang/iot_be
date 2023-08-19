# python
# -*- coding: UTF-8 -*-
"""
@Feat    ： 主蓝图的构造文件
@Project ：A-login-demo
@File    ：__init__.py
@Author  ：kaikai
@Date    ：2022/10/22 11:01
"""
from flask import Blueprint

main = Blueprint('main', __name__)  # 'main': 蓝本名称 __name__: 蓝本所在的包或模块

# 路由函数与错误处理函数最后导入以避免循环导入
from . import errors, views
