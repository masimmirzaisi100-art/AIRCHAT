import socket

ip = input("polease  Server IP enter: ") # 192.168.43.1 
s = socket.socket()
s.connect((ip, 1234))
print("[+] Connected!")

while True:
    data = s.recv(1024).decode()
    print(f"Dost: {data}")
    msg = input("You: ")
    s.send(msg.encode())
