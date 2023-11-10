import subprocess
import os
import tempfile
import shutil
from pyngrok import ngrok
import threading
import netifaces
#import Share

class WebServer:
    port = 8080
    server = None
    root = None
    ngrok=False
    ngrokUrls=[None]*2

    def getlocalip(self):
        iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
        return netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']

    def start(self):
        os.chdir(self.root.dir)
        self.server = subprocess.Popen(["python3", "-m", "http.server", str(self.port)],stdout=subprocess.PIPE)
        self.local=self.getlocalip()
        if(self.ngrok):
            ngrokLink=ngrok.connect(8056).__str__()
            tmp=ngrokLink.index("\"")+1
            tmp2=ngrokLink.index("\"",tmp+1)
            ngrokUrl1=ngrokLink[tmp:tmp2]
            link=ngrokUrl1[ngrokUrl1.rfind("/")+1:len(ngrokUrl1)]
            self.ngrokUrls[0]="http://"+link
            self.ngrokUrls[1]="https://"+link

    def __init__(self, port, root,ngrok):
        self.port = port
        self.root = root
        self.ngrok=ngrok

    def stop(self):
        self.server.kill()
        if(self.ngrok):
            for i in self.ngrokUrls:
                ngrok.disconnect(i)

class WebRoot:
    dir = ""

    def add_file_link(self, file):
        name = ""
        if os.name == "posix":
            name = file[file.rfind("/") + 1:len(file)]
        else:
            name = file[file.rfind("\\") + 1:len(file)]
        if not os.path.isfile(file):
            print("\""+file+"\" is not a valid file or argument")
            return
        os.symlink(os.path.abspath(file), self.dir+name)

    def add_file_cp(self,file):
        name = ""
        if os.name == "posix":
            name = file[file.rfind("/") + 1:len(file)]
        else:
            name = file[file.rfind("\\") + 1:len(file)]
        if not os.path.isfile(file):
            print("\""+file+"\" is not a valid file or argument")
            return
        shutil.copy(file, self.dir+name)

    def clean(self):
        shutil.rmtree(self.dir)

    def __init__(self):
        self.dir=tempfile.mkdtemp(prefix="Share_")+"/"
