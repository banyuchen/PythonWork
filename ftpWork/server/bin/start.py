import os
import sys
from server.core import server
import socketserver
from server.core.server import MyFTPServer

sys.path.append(os.path.dirname(os.getcwd()))

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), MyFTPServer)
    server.serve_forever()