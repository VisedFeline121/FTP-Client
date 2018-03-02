# -*- coding: utf-8 -*-
import socket
ENDING = "\r\n"
BITSIZE = 8
resp = {}
regex = r"[1-5]\d{2} .+((\n.+){1,2})?"
start_line = 'ftp> '
COMMANDS = """!               delete          literal         prompt          send
?               debug           ls              put             status
append          dir             mdelete         pwd             trace
ascii           disconnect      mdir            quit            type
bell            get             mget            quote           user
binary          glob            mkdir           recv            verbose
bye             hash            mls             remotehelp
cd              help            mput            rename
close           lcd             open            rmdir"""

class Client():
    def __init__(self):
        self.FTP_PORT = 21
        self.log_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def init_connection(self, ip):
        try:
            self.log_client_socket.connect((ip, self.FTP_PORT))
            self.log_client_socket.send("OPTS UTF8 ON\r\n")
            print self.log_client_socket.recv(1024),
            print self.log_client_socket.recv(1024),
            self.log_client_socket.send("USER " + raw_input("Input user name please: ") + ENDING)
            print self.log_client_socket.recv(1024),
            self.log_client_socket.send("PASS " + raw_input("Input password please: ") + ENDING)
            print self.log_client_socket.recv(1024),
            return True
        except:
            print "Unknown host"
            return False

    def get_response_on_command(self, num):
        with open('resps.txt') as res:
            for line in res:
                if line[0:3] == num:
                    print line[4:]
                    return line

    def AUTH(self, mechanism):
        self.log_client_socket.send("AUTH " + mechanism + ENDING)
        print self.log_client_socket.recv(1024),

    def ACCT(self):
        self.log_client_socket.send("ACCT" + ENDING)
        print self.log_client_socket.recv(1024),

    def ALLO(self):
        self.log_client_socket.send("ALLO" + ENDING)
        print self.log_client_socket.recv(1024),

    def APPE(self):
        self.log_client_socket.send("APPE" + ENDING)
        print self.log_client_socket.recv(1024),

    def CWD(self):
        self.log_client_socket.send("CWD" + ENDING)
        print self.log_client_socket.recv(1024),

    def DELE(self):
        self.log_client_socket.send("DELE" + ENDING)
        print self.log_client_socket.recv(1024),

    def FEAT(self):
        self.log_client_socket.send("FEAT" + ENDING)
        print self.log_client_socket.recv(1024),

    def LIT_HELP(self):
        self.log_client_socket.send("help" + ENDING)
        ret = self.log_client_socket.recv(1024)
        ret += self.log_client_socket.recv(1024)
        print ret[:-11]

    def LIST(self, argument=""):
        self.log_client_socket.send("NLST" + ENDING)
        print self.log_client_socket.recv(1024),

    def MODE(self):
        self.log_client_socket.send("MODE" + ENDING)
        print self.log_client_socket.recv(1024),

    def NLST(self):
        self.LIST()
        print self.log_client_socket.recv(1024),

    def NOOP(self):
        self.log_client_socket.send("NOOP" + ENDING)
        print self.log_client_socket.recv(1024),

    def OPTS(self):
        self.log_client_socket.send("OPTS" + ENDING)
        print self.log_client_socket.recv(1024),

    def PASSW(self):
        self.log_client_socket.send("PASSW" + ENDING)
        print self.log_client_socket.recv(1024),

    def PASV(self):
        self.log_client_socket.send("PASV" + ENDING)
        print self.log_client_socket.recv(1024),

    def PORT(self):
        self.log_client_socket.send("PORT" + ENDING)
        print self.log_client_socket.recv(1024),

    def QUIT(self):
        self.log_client_socket.send("QUIT" + ENDING)
        print self.log_client_socket.recv(1024),

    def REIN(self):
        self.log_client_socket.send("REIN" + ENDING)
        print self.log_client_socket.recv(1024),

    def REST(self):
        self.log_client_socket.send("REST" + ENDING)
        print self.log_client_socket.recv(1024),

    def REST_S(self):
        self.log_client_socket.send("REST_S" + ENDING)
        print self.log_client_socket.recv(1024),

    def RNFR(self):
        self.log_client_socket.send("RNFR" + ENDING)
        print self.log_client_socket.recv(1024),

    def RNTO(self):
        self.log_client_socket.send("RNTO" + ENDING)
        print self.log_client_socket.recv(1024),

    def SITE(self):
        self.log_client_socket.send("SITE" + ENDING)
        print self.log_client_socket.recv(1024),

    def STAT(self):
        self.log_client_socket.send("STAT" + ENDING)
        print self.log_client_socket.recv(1024),

    def STOR(self):
        self.log_client_socket.send("STOR" + ENDING)
        print self.log_client_socket.recv(1024),

    def STRU(self):
        self.log_client_socket.send("STRU" + ENDING)
        print self.log_client_socket.recv(1024),

    def TYPE(self):
        self.log_client_socket.send("TYPE" + ENDING)
        print self.log_client_socket.recv(1024),

    def USER(self):
        self.log_client_socket.send("USER" + ENDING)
        print self.log_client_socket.recv(1024),


def handle(client, com, status):
    if com[0] == 'help':
        print COMMANDS


def lit_handle(client, com):
    if com[0] == 'help':
        client.LIT_HELP()


def main():
    a = None
    commands = ['!', 'delete', 'literal', 'prompt', 'send',
                '?', 'debug', 'ls', 'put', 'status',
                'append', 'dir', 'mdelete', 'pwd', 'trace',
                'ascii', 'disconnect', 'mdir', 'quit', 'type',
                'bell', 'get', 'mget', 'quote', 'user',
                'binary', 'glob', 'mkdir', 'recv', 'verbose',
                'bye', 'hash', 'mls', 'remotehelp',
                'cd', 'help', 'mput', 'rename',
                'close', 'lcd', 'open', 'rmdir']
    connected = False
    ser = raw_input(start_line).split(" ")
    while ser[0] not in ['quit', 'bye']:
        if ser[0] == "open":
            if not connected:
                a = Client()
                if len(ser) == 1:
                    address = raw_input("To ")
                else:
                    address = ser[1]
                connected = a.init_connection(address)
            else:
                print "Already connected to a server, please disconnect first"
        if ser[0] == "close" and connected:
            a.QUIT()
            connected = False
        if ser[0] in commands:
            handle(a, ser, connected)
        else:
            print "invalid command"
        ser = raw_input(start_line).split(' ')
    if connected:
        a.QUIT()


if __name__ == '__main__':
    main()
