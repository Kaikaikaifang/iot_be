# python
# -*- coding: UTF-8 -*-
"""
@Project ：iot_be
@File    ：views.py
@Author  ：kaikai
@Date    ：2023/8/20 15:37 
"""
from . import api, socketio
from ..common import response, utils
from flask import request, current_app
from random import *
import os
import json


path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data.json')


@api.get('/')
def index():
    return response.success(message="Hi, this is a restful api server.", code=current_app.config["CODE"]["success"])

@api.post('/login')
def login():
    return response.success(request.json, code=2001)

@api.get('/data')
def data():
    return response.success(analyzed_data(get_data()), code=2001)

@api.post('/data')
def p_data():
    save_data(request.data.decode())
    socketio.emit('new_data', analyze_data(get_data()))
    print('send new data')
    return response.success(code=2001)

def get_data():
    with open(path, 'r', encoding="utf-8") as f:
        try:
            data=json.load(f)
            if data[-1]['times'] < 5:
                data.pop()
            data.reverse()        
        except json.JSONDecodeError:
            data = []
    return data[:15]

def save_data(data: str):
    with open(path, "r", encoding="utf-8") as f:
        try:
            existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = []
    if existing_data and existing_data[-1]['times'] < 5:
        existing_data[-1]['times'] += 1
        existing_data[-1]['data'] = existing_data[-1]['data'][:-6] + data
        existing_data[-1]['datetime'] = utils.getTs()
    else:
        existing_data.append({'times': 1, 'data': data, 'datetime': utils.getTs()})    
    with open(path, 'w') as file:
        json.dump(existing_data, file, indent=4)

def analyze_data(origin_data: list):
    analyzed_data = []
    for obj in origin_data:
        obj['SBP'] = int(obj['data'][1000:1002], 16)
        obj['DBP'] = int(obj['data'][1002:1004], 16)
        obj['HR'] = int(obj['data'][1004:1006], 16) 
        obj['PPG'] = []
        obj['ECG'] = []
        for t in range(5):
            for i in range(t*200, t*200+100, 4):
                obj['PPG'].append([i/4, int(curve[i:i+2], 16)*256 + int(curve[i+2:i+4], 16)])
                obj['ECG'].append([i/4, int(curve[i+100:i+102], 16)*256 + int(curve[i+102:i+104], 16)])
        analyzed_data.append(obj)
    return analyzed_data