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


app = create_app(os.getenv('FLASK_ENV', 'default'))