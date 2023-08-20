from . import socketio
from flask_socketio import emit

name_space = "/"

@socketio.on('connect', namespace=name_space)
def connected_msg():
    print('client connected.')


@socketio.on('disconnect', namespace=name_space)
def disconnect_msg():
    print('client disconnected.')