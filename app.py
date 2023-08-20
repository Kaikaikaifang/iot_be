# python
# -*- coding: UTF-8 -*-
"""
@Project ：A-login-demo 
@File    ：src.py
@Author  ：kaikai
@Date    ：2022/10/21 22:43
"""
import os
from src import create_app


app, socketio = create_app(os.getenv('FLASK_ENV', 'default'))


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True)