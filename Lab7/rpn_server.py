import socket
import sys

import RPNCalculator as rpn
    



HOST = ''
PORT = 7000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('# Socket created')
    s.bind((HOST, PORT))
    print('# Socket now listening')
    s.listen(10)
    conn, addr =s.accept()
    with conn:
        print('# Connected to ' + addr[0] + ':' + str(addr[1]))
        while True:
            data = conn.recv(1024)
            data = data.decode("UTF-8")
            if data.upper == "END":
                break
            conn.send(bytes(str(rpn.RPNCalulator(data)), "utf-8"))
    s.close()