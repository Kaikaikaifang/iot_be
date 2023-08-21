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


jsonAddr = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data.json')


@api.get('/')
def index():
    return response.success(message="Hi, this is a restful api server.", code=current_app.config["CODE"]["success"])

@api.post('/login')
def login():
    return response.success(request.json, code=2001)

def getData():
    with open(jsonAddr, 'r', encoding="utf-8") as f:
        try:
            data=json.load(f)
            data.reverse()        
        except json.JSONDecodeError:
            data = []
    return data[:15]

@api.get('/data')
def data():
    return response.success(getData(), code=2001)

@api.post('/data')
def p_data():
    PPG_Standard = [[0, 99], [14, 1800], [28, 3302], [42, 4172], [56, 3523], [70, 1848], [84, 586], [98, 2573], [112, 4098], [126, 3650], [140, -26], [154, -99], [168, 3276], [182, 4085], [196, 3559], [210, 1911], [224, 655], [238, 2675], [252, 4048], [266, 3777], [280, 55], [294, 32], [308, 3349], [322, 4190], [336, 3490], [350, 1989], [364, 649], [378, 2601], [392, 4048], [406, 3778], [420, -96], [434, 81], [448, 3349], [462, 4060], [476, 3560], [490, 1953], [504, 690], [518, 2620], [532, 4080], [546, 3750], [560, -25], [574, 5], [588, 3400], [602, 4081], [616, 3616], [630, 1886], [644, 700], [658, 2730], [672, 4116], [686, 3745]]
    ECG_Standard = [[0, 96], [14, 17685], [28, 34764], [42, 2865], [56, 18528], [70, 13860], [84, 27252], [98, 41234], [112, 50078], [126, 41759], [140, 9], [154, 17656], [168, 34663], [182, 2883], [196, 18641], [210, 13888], [224, 27426], [238, 41154], [252, 50190], [266, 41738], [280, 65], [294, 17778], [308, 34786], [322, 2981], [336, 18514], [350, 13972], [364, 27393], [378, 41206], [392, 50107], [406, 41728], [420, 68], [434, 17646], [448, 34842], [462, 2976], [476, 18590], [490, 13971], [504, 27410], [518, 41108], [532, 50222], [546, 41788], [560, -67], [574, 17776], [588, 34663], [602, 2998], [616, 18508], [630, 13963], [644, 27283], [658, 41196], [672, 50274], [686, 41767]]
    def saveJson(curve:str):
        SBP = 0
        DBP = 0
        HR = 0
        PPG_coordinate = []
        ECG_coordinate = []
        x=0
        SBP = int(curve[200:202], 16)
        DBP = int(curve[202:204], 16)
        HR = int(curve[204:206], 16)
        for i in range(0, 100, 4):
            PPG_coordinate.append([i, int(curve[i:i+2], 16)*256 + int(curve[i+2:i+4], 16)])
            ECG_coordinate.append([i, int(curve[i+50:i+52], 16)*256 + int(curve[i+52:i+54], 16)])

        data = {
            "SBP":SBP,  # 高压
            "DBP":DBP,  # 低压
            "HR": HR,  # 心率
            "PPG": PPG_coordinate,  # 脉搏图
            "ECG": ECG_coordinate,  # 心率图
            "V":randint(95,100),
            "datetime": utils.getTs(),
            "origin_data": curve
        }   
    
        with open(jsonAddr, "r", encoding="utf-8") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
        existing_data.append(data)
        with open(jsonAddr, 'w') as file:
            json.dump(existing_data, file, indent=4)
    saveJson(request.data.decode())
    socketio.emit('new_data', getData())
    print('send new data')
    return response.success(code=2001)