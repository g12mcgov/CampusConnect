## Runs Server

from campusconnect import application
from gevent import monkey
from socketio.server import SocketIOServer

monkey.patch_all()

if __name__ == '__main__':
	SocketIOServer(
		('', application.config['PORT']),
		application,
		resource="socket.io").server_forever()