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
times = 3

@api.get('/')
def index():
    return response.success(message="Hi, this is a restful api server.", code=current_app.config["CODE"]["success"])

@api.post('/login')
def login():
    return response.success(request.json, code=2001)

@api.get('/data')
def data():
    return response.success(analyze_data(get_data()), code=2001)

@api.post('/data')
def p_data():
    if save_data(request.data.decode()):
        socketio.emit('new_data', analyze_data(get_data()))
        print('send new data')
    return response.success(code=2001)

def get_data():
    with open(path, 'r', encoding="utf-8") as f:
        try:
            data=json.load(f)
            if data and data[-1]['times'] < times:
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
    if existing_data and existing_data[-1]['times'] < times:
        existing_data[-1]['times'] += 1
        existing_data[-1]['data'] = existing_data[-1]['data'][:-6] + data
        existing_data[-1]['datetime'] = utils.getTs()
    else:
        existing_data.append({'times': 1, 'data': data, 'datetime': utils.getTs()})    
    with open(path, 'w') as file:
        json.dump(existing_data, file, indent=4)
    return existing_data[-1]['times'] == times

def analyze_data(origin_data: list):
    analyzed_data = []
    for obj in origin_data:
        index = times * 200
        obj['SBP'] = int(obj['data'][index:index+2], 16)
        obj['DBP'] = int(obj['data'][index+2:index+4], 16)
        obj['HR'] = int(obj['data'][index+4:index+6], 16) 
        obj['PPG'] = []
        obj['ECG'] = []
        index = 0
        for t in range(times):
            for i in range(t*200, t*200+100, 4):
                obj['PPG'].append([index, int(obj['data'][i:i+2], 16)*256 + int(obj['data'][i+2:i+4], 16)])
                obj['ECG'].append([index, int(obj['data'][i+100:i+102], 16)*256 + int(obj['data'][i+102:i+104], 16)])
                index += 1
        analyzed_data.append(obj)
    return analyzed_data