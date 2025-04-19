import socket

# get ip of host server
ip = socket.gethostbyname('247ctf.com')
print(ip)
#                  # IPv4         # TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("247ctf.com",80))
s.sendall(b"HEAD / HTTP/1.1\r\nHost: 247ctf.com\r\n\r\n")
print(s.recv(1024).decode())
s.close()

client = False
server = False
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if server:
    s.bind(("127.0.0.1",port))
    s.listen()
    
    while True:
        connect, addr = s.accept()
        connect.send(b"You made it to the socket!")
        connect.close()

if client:
    s.connect(("127.0.0.1",port))
    print(s.recv(1024))
    s.close()

for port in [22,80,139,445,443,8080]:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex(("127.0.0.1", port))

    if result == 0:
        print(f"{port} is open.")
    else:
        print(f"{port} is closed.")