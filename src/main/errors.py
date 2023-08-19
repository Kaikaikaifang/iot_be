# python
# -*- coding: UTF-8 -*-
"""
@Project ：A-login-demo 
@File    ：errors.py
@Author  ：kaikai
@Date    ：2022/10/22 11:31 
"""
from . import main
from flask import request, jsonify


from flask import jsonify


@main.app_errorhandler(404)
def page_not_found(e):
    """404拦截器，防止flask直接返回默认页面
    :return { flask.Response }
    """
    response = jsonify({'message': 'resource not found', 'code': 404})
    response.status_code = 404
    return response


@main.app_errorhandler(405)
def method_not_allowed(e):
    """405拦截器
    :return { flask.Response }
    """
    response = jsonify({'message': 'method not allowed', 'code': 405})
    response.status_code = 405
    return response


@main.app_errorhandler(500)
def internal_server_error(e):
    """500拦截器
    :return { flask.Response }
    """
    response = jsonify({'message': 'internal server error', 'code': 500})
    response.status_code = 500
    return response


@main.app_errorhandler(400)
def bad_request_error(e):
    """400拦截器
    :return { flask.Response }
    """
    response = jsonify({'message': 'bad request error', 'code': 400})
    return response