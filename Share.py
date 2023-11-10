#!/usr/bin/python3
from WebServer import *
import sys
from PyQt5.QtWidgets import QDialog,QApplication
from SharingDialog import *

copy_mode=False
ngrok=False
port=8056
r=WebRoot()
c=1
term=True

class SharingDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sharing")
        self.parent=parent
        self.ui=Ui_SharingDialog()
        self.ui.setupUi(self)
        self.ui.stopSharing.clicked.connect(self.stopSharing)

    def stopSharing(self):
        self.done(0)

if len(sys.argv)==1:
        print("Nothing to share")
        exit(0) 

while c<len(sys.argv):
    i=sys.argv[c]
    

    if i=="-h" or i=="--help":
        print("Help")
        print("-------------------------")
        print("Usage:\n./Share.py <arguments> <files with method>")
        print("-------------------------")
        print("Arguments:")
        print("-h\t--help\tPrints this help message\n-p\t--port\tChange port in which the webserver will run. 8056 is default\n-ngrok\t--use-ngrok\tUse ngrok to forward local port to public ip. Use if u are behind a firewall\n-nt\t--no-term\tTo run GUI without terminal. Use when calling from other applications or as extension")
        print("-------------------------")
        print("Methods:")
        print("-cp\t--copy\tCopy the following files to webroot instead of linking them. Slower for large files. Use when linking is not possible\n-ln\t--link\tLinks the following files to webroot. Default method and need not be explicitly specified. Does not work in all cases")
        exit(0)
    elif i=="-cp" or i=="--copy":
        copy_mode=True
    elif i=="-ln" or i=="--link":
        copy_mode=False
    elif i=="-ngrok" or i=="--use-ngrok":
        ngrok=True
    elif i=="--no-term" or i=="-nt":
        term=False
    elif i=="-p" or i=="--port":
        c=c+1
        port=sys.argv[c]
    else:
        while (not ( i=="-cp" or i=="--copy" or i=="--link" or i=="-ln")) and c<len(sys.argv): 
            i=sys.argv[c]
            if copy_mode:
                 r.add_file_cp(i)
            else:
                 r.add_file_link(i)
            c=c+1
    c=c+1

w=WebServer(port,r,ngrok)
w.start()
if term:
    print("Local:\n"+w.local+":"+str(port))
    if ngrok:
        print("Public:")
        for i in w.ngrokUrls:
            print(i)
    input("\nPress enter to stop\n\nIncomming connections:\n")
else:
    app = QApplication(sys.argv)
    dialog=SharingDialog()
    if ngrok:
        dialog.ui.linkLabel.setText("Local:\n"+w.local+":"+str(port)+"\nPublic:\n"+w.ngrokUrls[0]+"\n"+w.ngrokUrls[1])
    else:
        dialog.ui.linkLabel.setText("Local:\n"+w.local+":"+str(port))
    dialog.exec_()
w.stop()
r.clean()
