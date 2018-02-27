# -*- coding: utf-8 -*-
import socket
import urllib2

ENDING = "\r\n"
BITSIZE = 8
resp = {}
regex = r"[1-5]\d{2} .+((\n.+){1,2})?"

class Client():
    def __init__(self, ip):
        self.FTP_IP = ip
        self.FTP_PORT = 21
        self.log_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log_client_socket.connect((self.FTP_IP, self.FTP_PORT))

    def get_response_on_command(self):
        num = self.log_client_socket.recv(3)

    def AUTH(self, mechanism):
        self.log_client_socket.send("AUTH " + mechanism + ENDING)

    def ACCT(self):
        self.log_client_socket.send("ACCT" + ENDING)

    def ALLO(self):
        self.log_client_socket.send("ALLO" + ENDING)

    def APPE(self):
        self.log_client_socket.send("APPE" + ENDING)

    def CWD(self):
        self.log_client_socket.send("CWD" + ENDING)

    def DELE(self):
        self.log_client_socket.send("DELE" + ENDING)

    def FEAT(self):
        self.log_client_socket.send("FEAT" + ENDING)

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
         self.log_client_socket.send("NLST" + ENDING)

    def MODE(self):
        self.log_client_socket.send("MODE" + ENDING)

    def NLST(self):
        self.LIST()

    def NOOP(self):
        self.log_client_socket.send("NOOP" + ENDING)

    def OPTS(self):
        self.log_client_socket.send("OPTS" + ENDING)

    def PASSW(self):
        self.log_client_socket.send("PASSW" + ENDING)

    def PASV(self):
        self.log_client_socket.send("PASV" + ENDING)

    def PORT(self):
        self.log_client_socket.send("PORT" + ENDING)

    def QUIT(self):
        self.log_client_socket.send("QUIT" + ENDING)

    def REIN(self):
        self.log_client_socket.send("REIN" + ENDING)

    def REST(self):
        self.log_client_socket.send("REST" + ENDING)

    def REST_S(self):
        self.log_client_socket.send("REST_S" + ENDING)

    def RNFR(self):
        self.log_client_socket.send("RNFR" + ENDING)

    def RNTO(self):
        self.log_client_socket.send("RNTO" + ENDING)

    def SITE(self):
        self.log_client_socket.send("SITE" + ENDING)

    def STAT(self):
        self.log_client_socket.send("STAT" + ENDING)

    def STOR(self):
        self.log_client_socket.send("STOR" + ENDING)

    def STRU(self):
        self.log_client_socket.send("STRU" + ENDING)

    def TYPE(self):
        self.log_client_socket.send("TYPE" + ENDING)

    def USER(self):
        self.log_client_socket.send("USER" + ENDING)
a = Client('demo.wftpserver.com')
a.log_client_socket.send("OPTS UTF8 ON\r\n")
a.log_client_socket.recv(1024)
a.log_client_socket.recv(1024)
a.log_client_socket.send("USER demo-user\r\n")
a.log_client_socket.recv(1024)
a.log_client_socket.send("PASS demo-user\r\n")
a.log_client_socket.recv(1024)
a.TYPE()
