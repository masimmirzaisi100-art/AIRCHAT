Me 



import socket

s = socket.socket()
s.bind(('0.0.0.0', 1234))
s.listen(1)
print("[+] Server ON. Dusra mobile connect hone ka wait kar raha...")
conn, addr = s.accept()
print(f"[+] Connected: {addr}")

while True:
    msg = input("You: ")
    conn.send(msg.encode())
    data = conn.recv(1024).decode()
    print(f"Dost: {data}")
