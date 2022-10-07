from flup.server.fcgi import WSGIServer
from website import create_app

app = create_app()

if __name__ == '__main__':
	WSGIServer(app, bindAddress=('127.0.0.1', 9000)).run()
