import socket

s = socket.socket()
s.bind(('0.0.0.0', 1234))
s.listen(1)
print("[+] Server ON.  second mobile connecting start process wait  ...")
conn, addr = s.accept()
print(f"[+] Connected: {addr}")

while True:
    msg = input("You: ")
    conn.send(msg.encode())
    data = conn.recv(1024).decode()
    print(f"friend: {data}")
