# socket producer.py
import socket, time
s = socket.socket()
s.connect(('localhost', 9999))

while True:
    now = int(time.time() * 1000)  # event time
    s.sendall(f"event_{now},{now}\n".encode())
    time.sleep(1)

