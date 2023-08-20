# python
# -*- coding: UTF-8 -*-
"""
@Project ：A-login-demo 
@File    ：views.py
@Author  ：kaikai
@Date    ：2022/11/16 15:37 
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
        data=json.load(f)
        keys=list(data.keys())
        vals=list(data.values())
        keys.reverse()
        vals.reverse()
        data=dict(zip(keys,vals))
        return data

@api.get('/data')
def data():
    return response.success(getData(), code=2001)

@api.post('/update')
def p_data():
    PPG_Standard = "[[0, 99], [14, 1800], [28, 3302], [42, 4172], [56, 3523], [70, 1848], [84, 586], [98, 2573], [112, 4098], [126, 3650], [140, -26], [154, -99], [168, 3276], [182, 4085], [196, 3559], [210, 1911], [224, 655], [238, 2675], [252, 4048], [266, 3777], [280, 55], [294, 32], [308, 3349], [322, 4190], [336, 3490], [350, 1989], [364, 649], [378, 2601], [392, 4048], [406, 3778], [420, -96], [434, 81], [448, 3349], [462, 4060], [476, 3560], [490, 1953], [504, 690], [518, 2620], [532, 4080], [546, 3750], [560, -25], [574, 5], [588, 3400], [602, 4081], [616, 3616], [630, 1886], [644, 700], [658, 2730], [672, 4116], [686, 3745]]"
    ECG_Standard = "[[0, 96], [14, 17685], [28, 34764], [42, 2865], [56, 18528], [70, 13860], [84, 27252], [98, 41234], [112, 50078], [126, 41759], [140, 9], [154, 17656], [168, 34663], [182, 2883], [196, 18641], [210, 13888], [224, 27426], [238, 41154], [252, 50190], [266, 41738], [280, 65], [294, 17778], [308, 34786], [322, 2981], [336, 18514], [350, 13972], [364, 27393], [378, 41206], [392, 50107], [406, 41728], [420, 68], [434, 17646], [448, 34842], [462, 2976], [476, 18590], [490, 13971], [504, 27410], [518, 41108], [532, 50222], [546, 41788], [560, -67], [574, 17776], [588, 34663], [602, 2998], [616, 18508], [630, 13963], [644, 27283], [658, 41196], [672, 50274], [686, 41767]]"
    def saveJson(curve:str):
        SBP = 0
        DBP = 0
        HR = 0
        curve = curve * 5
        PPG_coordinate = []
        ECG_coordinate = []
        x=0
        for index in range(0, len(curve), 14):
            SBP = int(curve[index+8:index+9 + 1], 16)
            DBP = int(curve[index+10:index+11 + 1], 16)
            HR = int(curve[index+12:index+13 + 1], 16)
            t1 = []
            t2 = []
            t1.append(x + index)
            t2.append(x+index)
            t1.append(int(curve[index:index + 2], 16)*256 + int(curve[index+2:index + 4], 16))  # 将16进制字符串转换成整数
            t2.append(int(curve[index+4:index + 6], 16)*256 + int(curve[index+6:index + 8], 16))
            PPG_coordinate.append(t1)
            ECG_coordinate.append(t2)
        event_time = utils.getTs()
        PPG_t = eval(PPG_Standard)
        for i in range(len(PPG_coordinate)):
            PPG_coordinate[i][1] = PPG_t[i][1] + randint(-1000,1000)
            if(PPG_coordinate[i][1]<0):
                PPG_coordinate[i][1] = 0
            ECG_coordinate[i][1] += randint(-100,100)
            if(ECG_coordinate[i][1] < 0):
                ECG_coordinate[i][1] = 0
        data = {
            event_time:{
                "SBP":SBP,  # 高压
                "DBP":DBP,  # 低压
                "HR": HR,  # 心率
                "PPG": PPG_coordinate,  # 脉搏图
                "ECG": ECG_coordinate,  # 心率图
                "V":randint(95,100),
            }
        }
    
        with open(jsonAddr, "r", encoding="utf-8") as f:
            file = f.read()
            if len(file)>0:
                old_data = json.loads(file)
            else:
                old_data = {}
            old_data.update(data)
        with open(jsonAddr, "w", encoding="utf-8") as f:
            # print(old_data)
            json.dump(old_data,f)
    saveJson(request.data.decode())
    socketio.emit('new_data', getData(), broadcast=False, namespace='/test')
    return response.success({'data': request.data.decode()}, code=2001)