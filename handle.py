# -*- coding: utf-8 -*-
import init_client
COMMANDS = """!               delete          literal         prompt          send
?               debug           ls              put             status
append          dir             mdelete         pwd             trace
ascii           disconnect      mdir            quit            type
bell            get             mget            quote           user
binary          glob            mkdir           recv            verbose
bye             hash            mls             remotehelp
cd              help            mput            rename
close           lcd             open            rmdir"""


def handle(client, com, status):
    if com[0] == '!':
        print "Goodbye"
    if com[0] == '?' and len(com) > 1:
        with open('helcom.txt') as f:
            for line in f:
                check = line.split(' ')[0]
                if com[1] == check:
                    print line
    if com[0] == 'append':
        pass
    if com[0] == 'ascii':
        pass
    if com[0] == 'bell':
        pass
    if com[0] == 'binary':
        pass
    if com[0] == 'bye':
        pass
    if com[0] == 'cd':
        pass
    if com[0] == 'close':
        client.Quit()
        status = False
    if com[0] == 'delete':
        pass
    if com[0] == 'dir':
        pass
    if com[0] == 'disconnect':
        pass
    if com[0] == 'get':
        pass
    if com[0] == 'glob':
        pass
    if com[0] == 'hash':
        pass
    if com[0] == 'lcd':
        pass
    if com[0] == 'literal':
        pass
    if com[0] == 'ls':
        pass
    if com[0] == 'mdelete':
        pass
    if com[0] == 'mdir':
        pass
    if com[0] == 'mget':
        pass
    if com[0] == 'mkdir':
        pass
    if com[0] == 'mls':
        pass
    if com[0] == 'mput':
        pass
    if com[0] == 'open':
        if not status:
                client = init_client.Client()
                if len(com) == 1:
                    address = raw_input("To ")
                else:
                    address = com[1]
                status = client.init_connection(address)
        else:
            print "Already connected to a server, please disconnect first"
    if com[0] == 'prompt':
        pass
    if com[0] == 'put':
        pass
    if com[0] == 'pwd':
        pass
    if com[0] == 'quit':
        pass
    if com[0] == 'quote':
        pass
    if com[0] == 'help' or (com[0] == '?' and len(com) == 1):
        print COMMANDS
    if com[0] == 'recv':
        pass
    if com[0] == 'remotehelp':
        pass
    if com[0] == 'rename':
        pass
    if com[0] == 'rmdir':
        pass
    if com[0] == 'send':
        pass
    if com[0] == 'status':
        pass
    if com[0] == 'trace':
        pass
    if com[0] == 'type':
        pass
    if com[0] == 'user':
        pass
    if com[0] == 'verbose':
        pass


def lit_handle(client, com):
    if com[0] == 'help':
        client.LIT_HELP()

def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()