import socket
import ssl

def web_body(device):

    html = """<html><head> <title>Maciej marczyszyn 249031</title> 
  <p>Device state: <strong>""" + device + """</strong></p>
  <p><a href="/?on"><button class="button">ON</button></a></p>
  <p><a href="/?off"><button class="button button2">OFF</button></a></p></body></html>"""
    html = bytes(html,"utf-8")
    return html

HOST = ''
PORT = 8000
device = "OFF"
with open("device.txt","r") as f:
    device = f.read()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    print('# Socket now listening')
    s.listen(10)
    while True:
        conn, addr =s.accept()
        with conn:
            request = conn.recv(1024).decode()
            print('Content = %s' % request)
            device_on = request.find('/?on')
            device_off = request.find('/?off')
            print(device_on)
            print(device_off)
            if device_on == 4:
                print('device ON')
                device = "ON"
            if device_off == 4:
                print('device OFF')
                device = "OFF"
            response = web_body(device)
            conn.send(b'HTTP/1.1 200 OK\n')
            conn.send(b'Content-Type: text/html\n')
            conn.send(b'Connection: close\n\n')
            conn.sendall(response)
            f = open("device.txt", "w")
            f.write(device)
            f.close()
            conn.close()
s.close()
