import tkinter as tk
from tkinter import messagebox
from ProjectManager import ProjectManagerPage
from ComponentManager import ComponentManagerPage
import sqlite3

class MenuBar(tk.Menu):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.create_menus()

    def create_menus(self):
        self.create_file_menu()
        self.create_db_menu()
        self.create_project_menu()

    def create_file_menu(self):
        file_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label='Dummy Option 1')
        file_menu.add_command(label='Dummy Option 2')
        file_menu.add_command(label='Exit', command=self.master.quit)

    def create_db_menu(self):
        db_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Database", menu=db_menu)
        db_menu.add_command(label='Component Manager', command=lambda: self.master.show_frame(ComponentManagerPage))
        db_menu.add_command(label='Test Connection', command=self.test_connection)

    def create_project_menu(self):
        project_menu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Projects", menu=project_menu)
        project_menu.add_command(label='Project Manager', command=lambda: self.master.show_frame(ProjectManagerPage))

    def test_connection(self):
        try:
            conn = sqlite3.connect("FV-Components.db")
            cursor = conn.cursor()
            cursor.execute('SELECT SQLITE_VERSION()')
            messagebox.showinfo("Success", f"Connected to ")
            conn.close()
        except Exception as e:
            messagebox.showinfo("Failure", "Database Connection Failed")
