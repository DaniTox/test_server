import socket
import threading
import sys

class Server:
  sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  connections = []
  
  def  __init__(self):
    self.sock.bind(('0.0.0.0', 10000))
    self.sock.listen(1)
    
  def handler(self, c, a):
    while True:
      data = c.recv(1024)
      for conn in self.connections:
        conn.send(data)
      if not data:
        self.connections.remove(c)
        c.close()
        break
        
        
  def run(self):
    while True:
      c, a = self.sock.accept()
      thr = threading.Thread(target=self.handler, args=(c, a))
      thr.daemon = True
      thr.start()
      self.connections.append(c)
      
      
      
class Client:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  def sendMsg(self):
    while True:
      self.sock.send(bytes(input(""), 'utf-8'))
      
  def __init__(self, address):
    self.sock.connect((address, 10000))
    
    thr = threading.Thread(target=sendMsg)
    thr.daemon = True
    thr.start()
    
    while True:
      data = self.sock.recv(1024)
      if not data:
        break
    
      
      
      
if (len(sys.argv) > 1):
  client = Client(sys.argv[1])
  
else:
  server = Server()
  server.run()
  
  
  
  
      
        
        
        