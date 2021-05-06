import socket

def http_get(target_host,target_port,save_file):
   
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    client.connect((target_host,target_port))  
    
    request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
    client.send(request.encode())  
    
    response = str(client.recv(4096), "utf-8")  

    with open (save_file, "w") as save:
        save.write(response)

http_get("www.youtube.com",80,"response.txt")
    
   