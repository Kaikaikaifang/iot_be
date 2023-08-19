# python
# -*- coding: UTF-8 -*-
"""
@Project ：A-login-demo 
@File    ：response.py
@Author  ：kaikai
@Date    ：2023/3/26 17:46 
"""
from flask import jsonify


def res(status_code=200, data=None, code=1, message="OK", decorate=True):
    """
    generate json response
    :param status_code: HTTP状态码 default 200
    :param data: 数据 default None
    :param code: API状态码 default 1
    :param message: 信息 default "OK"
    :param decorate: 是否包装 default True
    :return: flask.Response
    """
    if decorate:
        body = {'message': message, 'code': code}
        if data:
            body['data'] = data
    else:
        body = data
    response = jsonify(body)
    response.status_code = status_code
    return response


def success(data=None, code=1, message="OK", decorate=True):
    """200: 请求成功
    :param data: 数据 default None
    :param code: 状态码 default 1
    :param message: 信息 default "OK"
    :param decorate: 是否包装数据 default True
    :return: flask.Response
    """
    return res(200, data, code, message, decorate)


def created(data=None, code=1, message="Created", decorate=True):
    """201: 请求成功，并创建了一个新资源
    :param data: 数据 default None
    :param code: 状态码 default 1
    :param message: 信息 default "Created"
    :param decorate: 是否包装数据 default True
    :return: flask.Response
    """
    return res(201, data, code, message, decorate)


def accepted(data=None, code=1, message="Accepted", decorate=True):
    """202: 请求已接收，但仍在处理中，异步处理
    :param data: 数据 default None
    :param code: 状态码 default 1
    :param message: 信息 default "Accepted"
    :param decorate: 是否包装数据 default True
    :return: flask.Response
    """
    return res(202, data, code, message, decorate)


def no_content():
    """204: 请求成功处理，但响应无数据
    :return: flask.Response
    """
    return res(204, decorate=False)


def bad_req(code=400, message="Bad Request", decorate=True):
    """400: 坏请求，请求无效或不一致
    :param code: 状态码 default 1
    :param message: 信息 default "No Content"
    :param decorate: 是否包装数据 default True
    :return: flask.Response
    """
    return res(400, None, code, message, decorate)


def unauthorized(code=401, message="Unauthorized", decorate=True):
    """401: 未授权，身份凭证无效或未提供
    :param code: 状态码 default 401
    :param message: 信息 default "Unauthorized"
    :param decorate: 是否包装数据 default True
    :return: flask.Response
    """
    return res(401, None, code, message, decorate)


def forbidden(code=403, message="Forbidden", decorate=True):
    """403: 禁止，身份凭证无权访问指定资源
    :param code: 状态码 default 403
    :param message: 信息 default "Forbidden"
    :param decorate: 是否包装数据 default True
    :return: flask.Response
    """
    return res(403, None, code, message, decorate)


