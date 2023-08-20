# python
# -*- coding: UTF-8 -*-
"""
@Feat    ：主蓝本的路由函数
@Project ：A-login-demo 
@File    ：views.py
@Author  ：kaikai
@Date    ：2022/10/22 11:24
"""
from . import main
from ..common import response


@main.route('/', methods=['GET', 'POST'])
def index():
    return response.success(message="Hi, this is a restful api server, maybe you need to access url with prefix /api", code=2004)