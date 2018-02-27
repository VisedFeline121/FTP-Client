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
        self.trans_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log_client_socket.connect((self.FTP_IP, self.FTP_PORT))

    def get_response_on_command(self):
        num = self.log_client_socket.recv(3)

    def AUTH(self, mechanism):
        self.log_client_socket.send("AUTH " + mechanism + ENDING)

    def ACCT(self):
        pass

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
        pass

    def LIST(self):
        pass

    def MODE(self):
        pass

    def NLST(self):
        pass

    def NOOP(self):
        pass

    def OPTS(self):
        pass

    def PASSW(self, password=''):
        self.log_client_socket.send("PASS " + password + ENDING)

    def PASV(self):
        pass

    def PORT(self, port):
        my_ip = socket.gethostbyname(socket.gethostname())
        my_ip = my_ip.replace('.', ',')
        arg_high = port / 256
        arg_low = port % 256
        arg = my_ip + "," + str(arg_high) + "," + str(arg_low)
        self.log_client_socket.send("PORT " + arg + ENDING)
        self.trans_client_socket.connect((self.FTP_IP, port))

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

cl = Client('localhost')
cl.USER('ido')
cl.PASSW()
cl.PORT(33555)
