from flask import Blueprint
from .. import socketio

api = Blueprint('api', __name__)

# 路由函数与错误处理函数最后导入以避免循环导入
from . import views, errors
