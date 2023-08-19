# python
# -*- coding: UTF-8 -*-
"""
@Project ：A-login-demo 
@File    ：views.py
@Author  ：kaikai
@Date    ：2022/11/16 15:37 
"""
from . import api
from common import response
from flask import request, current_app


@api.get('/')
def index():
    return response.success(message="Hi, this is a restful api server.", code=current_app.config["CODE"]["success"])


@api.get('/data')
def data():
    return response.success({"success": 1}, code=2001)


@api.post('/data')
def p_data():
    print(request.json["hello"])
    return response.success(request.json, code=2001)