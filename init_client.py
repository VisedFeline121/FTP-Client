# -*- coding: utf-8 -*-
import socket
import platform
import handle
import thread

ENDING = "\r\n"
BITSIZE = 128
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
        self.ip = None
        self.type = 'I' # (I binary/A ascii)
        self.verbose = True
        self.bell = False
        self.prompt = True
        self.glob = True
        self.debug = False
        self.hash = False
        self.command_dict = {'AUTH': self.AUTH, 'ACCT': self.ACCT, 'ALLO': self.ALLO, 'APPE': self.APPE,
                             'CWD': self.CWD, 'DELE': self.DELE, 'FEAT': self.FEAT, 'HELP': self.HELP,
                             'LIST': self.LIST, 'MODE': self.MODE, 'NLST': self.NLST, 'NOOP': self.NOOP,
                             'OPTS': self.OPTS, 'PASS': self.PASS, 'PASV': self.PASV, 'PORT': self.PORT,
                             'QUIT': self.QUIT, 'REIN': self.REIN, 'REST': self.REST, 'RESTP': self.RESTP,
                             'RETR': self.RETR, 'RNFR': self.RNFR, 'RNTO': self.RNTO, 'SITE': self.SITE,
                             'STAT': self.STAT, 'STOR': self.STOR, 'STRU': self.STRU, 'TYPE': self.TYPE,
                             'USER': self.USER
        }
        self.status = False
        self.file_ended = False
        self.mode = 'ascii'
        self.log_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.trans_client_socket = None

    def connect(self, ip, port=21):
        self.ip = ip
        try:
            self.log_client_socket.connect((ip, int(port)))
            return self.log_client_socket.recv(BITSIZE)
        except Exception:
            return "Unknown host"

    def init_connection(self, ip):
        try:
            self.log_client_socket.connect((ip, self.FTP_PORT))
            self.log_client_socket.send("OPTS UTF8 ON\r\n")
            print self.log_client_socket.recv(BITSIZE),
            print self.log_client_socket.recv(BITSIZE),
            self.log_client_socket.send("USER " + raw_input("Input user name please: ") + ENDING)
            print self.log_client_socket.recv(BITSIZE),
            self.log_client_socket.send("PASS " + raw_input("Input password please: ") + ENDING)
            print self.log_client_socket.recv(BITSIZE),
            self.CWD('/')
            return True
        except:
            print "Unknown host"
            return False

    def get_response(self):
        return self.log_client_socket.recv(BITSIZE)

    def wait_to_end(self, name, t):
        ret = ''
        while ret == '':
            try:
                ret = self.log_client_socket.recv(BITSIZE)
            except:
                print 'Error occured'
        self.file_ended = True

    def get_response_on_command(self, num):
        with open('resps.txt') as res:
            for line in res:
                if line[0:3] == num:
                    print line[4:]
                    return line

    def set_mode(self, mode):
        if self.mode == mode[0]:
            print 'Already in ' + mode + ' mode'
        else:
            self.mode = mode[0]

    def AUTH(self, mechanism):
        self.log_client_socket.send("AUTH " + mechanism[0] + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def ACCT(self):
        self.log_client_socket.send("ACCT" + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def ALLO(self):
        self.log_client_socket.send("ALLO" + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def APPE(self):
        self.log_client_socket.send("APPE" + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def CWD(self, path):
        self.log_client_socket.send("CWD " + path[0] + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def DELE(self, name):
        self.log_client_socket.send("DELE " + name[0] + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def FEAT(self):
        self.log_client_socket.send("FEAT" + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def HELP(self):
        self.log_client_socket.send("help" + ENDING)
        ret = self.log_client_socket.recv(BITSIZE)
        ret = 'aaa'
        while ret[0:3] != '214':
            ret = self.log_client_socket.recv(BITSIZE)
            print ret,

    def LIST(self):
        ip, port = self.PASV()
        self.log_client_socket.send('LIST' + ENDING)
        print self.log_client_socket.recv(BITSIZE)
        self.trans_client_socket.connect((ip, port))
        files = self.trans_client_socket.recv(BITSIZE)
        print self.log_client_socket.recv(BITSIZE)
        self.trans_client_socket.close()
        return files

    def MODE(self):
        self.log_client_socket.send("MODE" + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def NLST(self):
        ip, port = self.PASV()
        self.log_client_socket.send('NLST' + ENDING)
        print self.log_client_socket.recv(BITSIZE)
        self.trans_client_socket.connect((ip, port))
        files = self.trans_client_socket.recv(BITSIZE)
        print self.log_client_socket.recv(BITSIZE)
        self.trans_client_socket.close()
        return files

    def NOOP(self):
        self.log_client_socket.send('NOOP' + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def OPTS(self, params):
        self.log_client_socket.send("OPTS " + params[0] + ' ' + params[1] + ENDING)
        return self.get_response()

    def PASS(self, password):
        self.log_client_socket.send("PASS " + password[0] + ENDING)
        ret = self.log_client_socket.recv(BITSIZE)
        if ret[:3] == '230':
            self.status = True
        return ret

    def PASV(self):
        self.trans_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log_client_socket.send("PASV" + ENDING)
        response = self.log_client_socket.recv(1024)
        print response, response, response
        response = response.split('(')[1][:-3]
        ip = '.'.join(response.split(',')[0:4])
        port = response.split(',')[4:]
        port = int(port[0]) * 256 + int(port[1])
        return ip, port


    def PORT(self, port=[44444]):
        my_ip = socket.gethostbyname(socket.gethostname())
        my_ip = my_ip.replace('.', ',')
        arg_high = int(port[0]) / 256
        arg_low = int(port[0]) % 256
        arg = my_ip + "," + str(arg_high) + "," + str(arg_low)
        self.trans_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log_client_socket.send("PORT " + arg + ENDING)
        self.trans_client_socket.connect((self.ip, int(port[0])))
        return self.log_client_socket.recv(BITSIZE)

    def QUIT(self):
        self.log_client_socket.send("QUIT" + ENDING)
        ret =  self.log_client_socket.recv(BITSIZE)
        self.log_client_socket.close()
        return ret

    def REIN(self):
        self.log_client_socket.send("REIN" + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def REST(self):
        self.log_client_socket.send("REST" + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def RESTP(self):
        self.log_client_socket.send("REST+" + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def RETR(self, names):
        self.PASV()
        self.log_client_socket.send("RETR " + names[1] + ENDING)
        ret = self.log_client_socket.recv(BITSIZE)
        ans = ''
        thread.start_new_thread(self.wait_to_end, ('myThread', 1,))
        if ret[:3] != '150':
            return ret
        else:
            with open(names[0], 'ab') as a:
                while not self.file_ended:
                    ret = self.trans_client_socket.recv(1460)
                    a.write(ret)
        self.trans_client_socket.close()

    def RNFR(self, names):
        self.log_client_socket.send("RNFR " + names[0] + ENDING)
        msg = self.log_client_socket.recv(BITSIZE)
        msg2 = self.RNTO(names[1])
        return msg + msg2

    def RNTO(self, name):
        self.log_client_socket.send("RNTO " + name[0] + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def SITE(self):
        self.log_client_socket.send("SITE" + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def STAT(self, type, verbose, bell, prompting, globbing, debugging, hash):
        print 'Type: {}; Verbose: {}; Bell: {}; Prompting: {}; Globbing: On Debugging: {}; Hash mark printing: {}'\
            .format(type, verbose, bell, prompting, globbing, debugging, hash)

    def STOR(self, names):  # put/send
        self.PASV()
        ret = self.log_client_socket.send("STOR " + names[1] + ENDING)
        if ret[0:3] != '150':
            return self.log_client_socket.recv(BITSIZE)
        else:
            with open(names[0], 'rb') as a:
                for line in a:
                    self.trans_client_socket.send(line)
            return self.trans_client_socket.recv(BITSIZE)

    def STRU(self):
        self.log_client_socket.send("STRU" + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def TYPE(self, type):
        self.log_client_socket.send("TYPE " + type[0] + ENDING)
        return self.log_client_socket.recv(BITSIZE)

    def USER(self, user_name):
        self.log_client_socket.send("USER " + user_name[0] + ENDING)
        return self.log_client_socket.recv(BITSIZE)


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
