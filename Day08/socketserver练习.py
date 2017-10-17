__author__ = "xiaoyu hao"

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                #连接客户端 self.request is the TCP socket connected to the client，recv接收
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                #发送数据
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err",e)
                break
if __name__ == "__main__":
    host = "localhost"
    port = 1234
    ADDR = (host, port)
    # Create the server, binding to localhost on port 1234
    server = socketserver.ThreadingTCPServer(ADDR, MyTCPHandler)
    #Activate the server;
    server.serve_forever()