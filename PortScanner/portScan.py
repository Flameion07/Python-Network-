import socket

target = " 127.0.0.1"
a=int("10")
for i in range(500):
    a+=10

def portScan(port):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        return True
    except:
        return False

print(portScan(a))
print(a)
    
