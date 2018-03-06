# -*- coding: utf-8 -*-
import socket
import platform
import handle

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
        self.command_dict = {'AUTH': self.AUTH, 'ACCT': self.ACCT, 'ALLO': self.ALLO, 'APPE': self.APPE,
                             'CWD': self.CWD, 'DELE': self.DELE, 'FEAT': self.FEAT, 'HELP': self.HELP,
                             'LIST': self.LIST, 'MODE': self.MODE, 'NLST': self.NLST, 'NOOP': self.NOOP,
                             'OPTS': self.OPTS, 'PASS': self.PASS, 'PASV': self.PASV, 'PORT': self.PORT,
                             'QUIT': self.QUIT, 'REIN': self.REIN, 'REST': self.REST, 'RESTP': self.RESTP,
                             'RETR': self.RETR, 'RNFR': self.RNFR, 'SITE': self.SITE, 'STAT': self.STAT,
                             'STOR': self.STOR, 'STRU': self.STRU, 'TYPE': self.TYPE, 'USER': self.USER
        }
        self.status = False
        self.mode = 'ascii'
        self.FTP_PORT = 21
        self.log_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.trans_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, ip):
        try:
            self.log_client_socket.connect((ip, self.FTP_PORT))
            return self.log_client_socket.recv(1024)
        except:
            return "Unknown host"

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
            self.CWD('/')
            return True
        except:
            print "Unknown host"
            return False

    def get_response(self):
        return self.log_client_socket.recv(1024)

    def get_response_on_command(self, num):
        with open('resps.txt') as res:
            for line in res:
                if line[0:3] == num:
                    print line[4:]
                    return line

    def set_mode(self, mode):
        if self.mode == mode:
            print 'Already in ' + mode + ' mode'
        else:
            self.mode = mode

    def AUTH(self, mechanism):
        self.log_client_socket.send("AUTH " + mechanism + ENDING)
        return self.log_client_socket.recv(1024)

    def ACCT(self):
        self.log_client_socket.send("ACCT" + ENDING)
        return self.log_client_socket.recv(1024)

    def ALLO(self):
        self.log_client_socket.send("ALLO" + ENDING)
        return self.log_client_socket.recv(1024)

    def APPE(self):
        self.log_client_socket.send("APPE" + ENDING)
        return self.log_client_socket.recv(1024)

    def CWD(self, path):
        self.log_client_socket.send("CWD " + path + ENDING)
        return self.log_client_socket.recv(1024)

    def DELE(self, name):
        self.log_client_socket.send("DELE " + name + ENDING)
        return self.log_client_socket.recv(1024)

    def FEAT(self):
        self.log_client_socket.send("FEAT" + ENDING)
        return self.log_client_socket.recv(1024)

    def HELP(self):
        self.log_client_socket.send("help" + ENDING)
        ret = log_client_socket.recv(1024)
        ret = 'aaa'
        while ret[0:3] != '214':
            ret = log_client_socket.recv(1024)
            print ret,

    def LIST(self):
        self.PORT()
        self.log_client_socket.send("LIST" + ENDING)
        ret = self.log_client_socket.recv(1024)
        while ret[0:3] != 226:
            ret = self.log_client_socket.recv(1024)

    def MODE(self):
        self.log_client_socket.send("MODE" + ENDING)
        return self.log_client_socket.recv(1024)

    def NLST(self):
        self.PORT()
        log_client_socket.send('NLST' + ENDING)
        ret = self.log_client_socket.recv(1024)
        while ret[0:3] != 226:
            ret = self.log_client_socket.recv(1024)

    def NOOP(self):
        log_client_socket.send('NOOP' + ENDING)
        print log_client_socket.recv(1024)

    def OPTS(self, mode, of):
        self.log_client_socket.send("OPTS " + mode + ' ' + of + ENDING)
        return self.log_client_socket.recv(1024)

    def PASS(self, password):
        self.log_client_socket.send("PASS " + password + ENDING)
        ret = self.log_client_socket.recv(1024)
        if ret[0:3] == '230':
            self.status = True

    def PASV(self):
        self.log_client_socket.send("PASV" + ENDING)
        return self.log_client_socket.recv(1024)

    def PORT(self, port):
        my_ip = socket.gethostbyname(socket.gethostname())
        my_ip = my_ip.replace('.', ',')
        arg_high = port / 256
        arg_low = port % 256
        arg = my_ip + "," + str(arg_high) + "," + str(arg_low)
        self.log_client_socket.send("PORT " + arg + ENDING)
        self.trans_client_socket.connect((self.FTP_IP, port))
        return self.log_client_socket.recv(1024)

    def QUIT(self):
        self.log_client_socket.send("QUIT" + ENDING)
        return self.log_client_socket.recv(1024)
        self.log_client_socket.close()

    def REIN(self):
        self.log_client_socket.send("REIN" + ENDING)
        return self.log_client_socket.recv(1024)

    def REST(self):
        self.log_client_socket.send("REST" + ENDING)
        return self.log_client_socket.recv(1024)

    def RESTP(self):
        self.log_client_socket.send("REST+" + ENDING)
        return self.log_client_socket.recv(1024)

    def RETR(self, local_name, remote_name):
        ret = self.log_client_socket.send("RETR " + remote_name + ENDING)
        if ret[0:3] != '150':
            return self.log_client_socket.recv(1024)
        else:
            with open(local_name) as a:
                while ret[0:3] != 226:
                    ret = log_client_socket.recv(BITSIZE)
                    if ret[0:3] != 226:
                        a.write(ret)

    def RNFR(self, name, new_name):
        self.log_client_socket.send("RNFR " + name + ENDING)
        return self.log_client_socket.recv(1024)
        self.log_client_socket.send("RNTO " + new_name + ENDING)
        return self.log_client_socket.recv(1024)

    def SITE(self):
        self.log_client_socket.send("SITE" + ENDING)
        return self.log_client_socket.recv(1024)

    def STAT(self, type, verbose, bell, prompting, globbing, debugging, hash):
        print 'Type: {}; Verbose: {}; Bell: {}; Prompting: {}; Globbing: On Debugging: {}; Hash mark printing: {}'\
            .format(type, verbose, bell, prompting, globbing, debugging, hash)

    def STOR(self, local_name, remote_name):  # put/send
        ret = self.log_client_socket.send("STOR " + remote_name + ENDING)
        if ret[0:3] != '150':
            return self.log_client_socket.recv(1024)
        else:
            with open(local_name) as a:
                for line in a:
                    self.log_client_socket.send(line)
            return self.log_client_socket.recv(1024)

    def STRU(self):
        self.log_client_socket.send("STRU" + ENDING)
        return self.log_client_socket.recv(1024)

    def TYPE(self, type):
        self.log_client_socket.send("TYPE " + type + ENDING)
        return self.log_client_socket.recv(1024)

    def USER(self, user_name):
        self.log_client_socket.send("USER " + user_name + ENDING)
        return self.log_client_socket.recv(1024)


def main():
    a = None
    commands = ['!', 'delete', 'literal', 'prompt', 'send',
                '?', 'debug', 'ls', 'put', 'status', 'port',
                'append', 'dir', 'mdelete', 'pwd', 'trace',
                'ascii', 'disconnect', 'mdir', 'quit', 'type',
                'bell', 'get', 'mget', 'quote', 'user',
                'binary', 'glob', 'mkdir', 'recv', 'verbose',
                'bye', 'hash', 'mls', 'remotehelp',
                'cd', 'help', 'mput', 'rename',
                'close', 'lcd', 'open', 'rmdir']
    connected = False
    ser = 'None'
    while ser[0] not in ['quit', 'bye']:
        ser = raw_input(start_line).split(' ')
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
            handle.handle(a, ser, connected)
        else:
            print "invalid command"
    if connected:
        a.QUIT()


if __name__ == '__main__':
    main()
