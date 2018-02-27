# -*- coding: utf-8 -*-
import Tkinter as tk
import ScrolledText
import logging
from ttk import Treeview


class TextHandler(logging.Handler):
    def __init__(self, text):
        logging.Handler.__init__(self)
        self.text = text

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            self.text.yview(tk.END)

        self.text.after(0, append)


class Client(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.master.minsize(800, 600)
        self.master.title("FTP Client")

        self.menu_bar = tk.Menu(self.master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)

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

        self.master.option_add("*tearOff", 'False')

        self.st = ScrolledText.ScrolledText(self.master, state='disabled')
        self.st.configure(font=('TkFixedFont', 16), height=7)
        self.st.grid(column=0, row=1, sticky='nwe', columnspan=9)

        self.text_handler = TextHandler(self.st)

        logging.basicConfig(filename='test.log',
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        self.logger = logging.getLogger()
        self.logger.addHandler(self.text_handler)

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
        self.host_label = tk.Label(self.master, text="Host:").grid(row=0, column=0)
        self.host_entry = tk.Entry(self.master).grid(row=0, column=1)

        self.user_label = tk.Label(self.master, text="Username:").grid(row=0, column=2)
        self.user_entry = tk.Entry(self.master).grid(row=0, column=3)

        self.password_label = tk.Label(self.master, text="Password:").grid(row=0, column=4)
        self.password_entry = tk.Entry(self.master, show="*").grid(row=0, column=5)

        self.port_label = tk.Label(self.master, text="Port:").grid(row=0, column=6)
        self.port_entry = tk.Entry(self.master).grid(row=0, column=7)

        self.connect_button = tk.Button(self.master, text="Connect", command=None).grid(row=0, column=8)

    def create_user_tree(self):
        self.user_tree = Treeview(self.master)
        self.user_tree.heading("#0", text="Current Local Directory: {}".format(''))
        self.user_tree.grid(row=2, columnspan=4, sticky='nswe')

    def create_server_tree(self):
        self.server_tree = Treeview(self.master)
        self.server_tree.heading("#0", text="Current Server Directory: {}".format(''))
        self.server_tree.grid(row=2, column=4, columnspan=5, sticky='nswe')

    def create_arbitrary_command(self):
        self.command_label = tk.Label(self.master,
                                      text="Send Arbitrary Command:").grid(row=3, column=0)
        self.command_entry = tk.Entry(self.master).grid(row=3, column=1)
        self.command_button = tk.Button(self.master, text="Send Command", command=None).grid(row=3, column=2)

    def insert_dirs_to_tree(self, tree, parent_id, dir_id, content):
        for i in content:
            tree.insert(parent_id, 'end', dir_id, text=i)

    def insert_files_to_tree(self, tree, parent_id, content):
        for i in content:
            tree.insert(parent_id, 'end', text=i)

    def run(self):
        self.master.mainloop()


def main():
    master = tk.Tk()
    app = Client(master)
    app.run()


if __name__ == '__main__':
    main()
