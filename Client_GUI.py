# -*- coding: utf-8 -*-
import Tkinter as Tk
import ScrolledText
import logging
from ttk import Treeview
from init_client import Client
from os import listdir
from os.path import isfile, join
import _tkinter

PATH = r'C:\Users\IDO\Desktop'


class TextHandler(logging.Handler):
    def __init__(self, text):
        logging.Handler.__init__(self)
        self.text = text

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text.configure(state='normal')
            self.text.insert(Tk.END, msg + '-' * 100 + '\n')
            self.text.configure(state='disabled')
            self.text.yview(Tk.END)

        self.text.after(0, append)


class ClientGUI(Tk.Frame):
    def __init__(self, master):
        Tk.Frame.__init__(self, master)
        self.master = master

        self.master.minsize(800, 600)
        self.master.title("FTP Client")

        self.menu_bar = Tk.Menu(self.master)
        self.file_menu = Tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu = Tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu = Tk.Menu(self.menu_bar, tearoff=0)

        self.command_label = None
        self.command_entry = None
        self.command_button = None
        self.user_tree = None
        self.server_tree = None
        self.host_entry = None
        self.host_label = None
        self.user_entry = None
        self.user_label = None
        self.password_entry = None
        self.password_label = None
        self.port_entry = None
        self.port_label = None
        self.connect_button = None

        self.host_var = Tk.StringVar(self.master, value='localhost')
        self.user_var = Tk.StringVar(self.master, value='user')
        self.password_var = Tk.StringVar(self.master, value='pass')
        self.port_var = Tk.StringVar(self.master, value='21')
        self.command_var = Tk.StringVar(self.master, value='retr sup.txt sup.txt')
        self.local_dir_var = 'Desktop'

        self.master.option_add("*tearOff", 'False')

        self.st = ScrolledText.ScrolledText(self.master, state='disabled')
        self.st.configure(font=('TkFixedFont', 8), height=7)
        self.st.grid(column=0, row=1, sticky='nwe', columnspan=9)

        self.text_handler = TextHandler(self.st)

        logging.basicConfig(filename='test.log',
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        self.logger = logging.getLogger()
        self.logger.addHandler(self.text_handler)

        self.client = Client()

        self.create_menu_bar()
        self.create_connection_widgets()
        self.create_user_tree()
        self.create_server_tree()
        self.create_arbitrary_command()

    def create_menu_bar(self):
        self.file_menu.add_command(label="Settings", command=None)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu.add_command(label="To be added", command=None)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        self.help_menu.add_command(label="Help", command=None)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="About", command=None)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        self.master.config(menu=self.menu_bar)

    def create_connection_widgets(self):
        self.host_label = Tk.Label(self.master, text="Host:").grid(row=0, column=0)
        self.host_entry = Tk.Entry(self.master, textvariable=self.host_var).grid(row=0, column=1)

        self.user_label = Tk.Label(self.master, text="Username:").grid(row=0, column=2)
        self.user_entry = Tk.Entry(self.master, textvariable=self.user_var).grid(row=0, column=3)

        self.password_label = Tk.Label(self.master, text="Password:").grid(row=0, column=4)
        self.password_entry = Tk.Entry(self.master, textvariable=self.password_var, show="*").grid(row=0, column=5)

        self.port_label = Tk.Label(self.master, text="Port:").grid(row=0, column=6)
        self.port_entry = Tk.Entry(self.master, textvariable=self.port_var).grid(row=0, column=7)

        self.connect_button = Tk.Button(self.master, text="Connect",
                                        command=lambda: self.init_socket_connection()).grid(row=0, column=8)

    def create_user_tree(self):
        self.user_tree = Treeview(self.master)
        self.user_tree.heading("#0", text="Current Local Directory: {}".format(self.local_dir_var))

        list_of_dirs = [d for d in listdir(PATH) if not isfile(join(PATH, d))]
        self.user_tree.insert('', 'end', PATH, text='Desktop')
        self.recursive_dirs(PATH, list_of_dirs)
        self.user_tree.tag_bind('dir', '<1>', self.change_header)
        self.user_tree.grid(row=2, columnspan=4, sticky='nswe')

    def create_server_tree(self):
        self.server_tree = Treeview(self.master)
        self.server_tree.heading("#0", text="Current Server Directory: {}".format(''))
        self.server_tree.grid(row=2, column=4, columnspan=5, sticky='nswe')

    def create_arbitrary_command(self):
        self.command_label = Tk.Label(self.master,
                                      text="Send Arbitrary Command:").grid(row=3, column=0)
        self.command_entry = Tk.Entry(self.master, textvariable=self.command_var).grid(row=3, column=1)
        self.command_button = Tk.Button(self.master, text="Send Command", command=self.add_to_log).grid(row=3, column=2)

    def insert_dirs_to_tree(self, tree, parent_id, dir_id, content):
        for i in content:
            try:
                tree.insert(parent_id, 'end', join(dir_id, i), text=i, tags=('dir'))
            except _tkinter.TclError:
                tree.insert(join(parent_id, dir_id), 'end', join(dir_id, i), text=i)

    def insert_files_to_tree(self, tree, parent_id, content):
        for i in content:
            tree.insert(parent_id, 'end', text=i)

    def init_socket_connection(self):
        if self.port_var.get() != '':
            logging.info(self.client.connect(self.host_var.get(), self.port_var.get()))
        else:
            logging.info(self.client.connect(self.host_var.get()))
        #logging.info(self.client.OPTS(['UTF8', 'ON']))
        logging.info(self.client.USER([self.user_var.get()]))
        logging.info(self.client.PASS([self.password_var.get()]))
        logging.info(self.client.CWD(['/']))

    def add_to_log(self):
        logging.info(self.send_command())

    def send_command(self):
        raw_command = self.command_var.get()
        raw_command = raw_command.split(' ')
        command = raw_command[0]
        command = command.upper()
        command = self.client.command_dict[command]
        if len(raw_command) > 1:
            params = raw_command[1:]
            return command(params)
        else:
            return command()

    def run(self):
        self.master.mainloop()

    def recursive_dirs(self, dir_path, current_dirs):
        files_in_dir = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
        for a_dir in current_dirs:
            this_dir_path = join(dir_path, a_dir)

            new_dirs = [d for d in listdir(this_dir_path) if not isfile(join(this_dir_path, d))]
            self.insert_dirs_to_tree(self.user_tree, dir_path, this_dir_path, new_dirs)
            self.recursive_dirs(this_dir_path, new_dirs)

        try:
            self.insert_files_to_tree(self.user_tree, dir_path, files_in_dir)
        except:
            pass

    def change_header(self, event):
        self.local_dir_var = self.user_tree.focus()
        self.user_tree.heading('#0', text=self.local_dir_var)


def main():
    master = Tk.Tk()
    app = ClientGUI(master)
    app.run()


if __name__ == '__main__':
    main()