# -*- coding: utf-8 -*-
import socket
import time

ENDING = "\r\n"
BITSIZE = 8
resp = {}
regex = r"[1-5]\d{2} .+((\n.+){1,2})?"

class Client():
    def __init__(self, ip):
        self.FTP_IP = ip
        self.FTP_PORT = 21
        self.data_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log_client_socket.connect((self.FTP_IP, self.FTP_PORT))

    def get_response_on_command(self):
        num = self.log_client_socket.recv(3)


    def AUTH(self, mechanism):
        self.log_client_socket.send("AUTH " + mechanism + ENDING)

    def ACCT(self):
        self.log_client_socket.send("ACCT" + ENDING)

    def ALLO(self):
        pass

    def APPE(self):
        pass

    def CWD(self):
        pass

    def DELE(self):
        pass

    def FEAT(self):
        pass

    def HELP(self):
        print """!               delete          literal         prompt          send
?               debug           ls              put             status
append          dir             mdelete         pwd             trace
ascii           disconnect      mdir            quit            type
bell            get             mget            quote           user
binary          glob            mkdir           recv            verbose
bye             hash            mls             remotehelp
cd              help            mput            rename
close           lcd             open            rmdir"""

    def LIT_HELP(self):
        self.log_client_socket.send("help" + ENDING)

    def LIST(self):
         self.log_client_socket.send("NLST")

    def MODE(self):
        pass

    def NLST(self):
        self.LIST()

    def NOOP(self):
        pass

    def OPTS(self):
        pass

    def PASSW(self, password=''):
        self.log_client_socket.send("PASS " + password + ENDING)
        print self.log_client_socket.recv(1024)

    def PASV(self):
        self.log_client_socket.send("PASV" + ENDING)
        response = self.log_client_socket.recv(1024)
        print response
        response = response.split('(')[1][:-3]
        ip = '.'.join(response.split(',')[0:4])
        port = response.split(',')[4:]
        port = int(port[0]) * 256 + int(port[1])
        self.data_client_socket.connect((ip, port))

    def PORT(self, port):
        my_ip = socket.gethostbyname(socket.gethostname())
        my_ip = my_ip.replace('.', ',')
        arg_high = port / 256
        arg_low = port % 256
        arg = '127,0,0,1' + "," + str(arg_high) + "," + str(arg_low)
        #self.data_client_socket.bind(('0.0.0.0', port))
        #self.data_client_socket.listen(1)
        self.log_client_socket.send("PORT " + arg + ENDING)
        print self.log_client_socket.recv(1024)
        #conn, addr = self.data_client_socket.accept()

    def QUIT(self):
        pass

    def REIN(self):
        pass

    def REST(self):
        pass

    def REST_S(self):
        pass

    def RNFR(self):
        pass

    def RNTO(self):
        pass

    def SITE(self):
        pass

    def STAT(self):
        pass

    def STOR(self):
        pass

    def STRU(self):
        pass

    def TYPE(self):
        pass

    def USER(self, username):
        self.log_client_socket.send('USER ' + username + ENDING)
        print self.log_client_socket.recv(1024)

cl = Client('localhost')
cl.USER('user')
cl.PASSW('pass')
#while True:
#    pass
#cl.PORT(33555)
cl.PASV()
