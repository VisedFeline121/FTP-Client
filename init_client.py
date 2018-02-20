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
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.FTP_IP, self.FTP_PORT))

    def get_response_on_command(self):
        num = self.client_socket.recv(3)


    def AUTH(self, mechanism):
        self.client_socket.send("AUTH " + mechanism + ENDING)

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

    def PASSW(self):
        pass

    def PASV(self):
        pass

    def PORT(self):
        pass

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

    def USER(self):
        pass
