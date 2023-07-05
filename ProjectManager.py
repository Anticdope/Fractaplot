import tkinter as tk
from tkinter import ttk, messagebox
from DatabaseManager import DatabaseManager

class ProjectManagerPage(tk.Frame):
    
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.db_manager = DatabaseManager('FV-Components.db')
        self.component_order = []
        self.components = {}
        self.configure_grid()

        self.create_labels()
        self.create_dropdown()
        self.create_radiobuttons()
        self.create_entry()
        self.create_buttons()
        self.create_treeview()

    def configure_grid(self):
        for i in range(10):
            self.grid_columnconfigure(i, weight=1)
        for i in range(20):
            self.grid_rowconfigure(i, weight=1 if i < 10 else 3)

    def create_labels(self):
        tk.Label(self, text="Component Type").grid(row=0, column=1)
        tk.Label(self, text="Generic or Custom").grid(row=2, column=1)
        tk.Label(self, text="Component ID").grid(row=6, column=1)

    def create_dropdown(self):
        self.component_var = tk.StringVar()
        self.component_dropdown = ttk.Combobox(self, textvariable=self.component_var)
        self.component_dropdown['values'] = self.db_manager.get_table_names()
        self.component_dropdown.grid(row=1, column=1)

    def create_radiobuttons(self):
        self.type_var = tk.StringVar(value='Generic')
        ttk.Radiobutton(self, text='Generic', variable=self.type_var, value='Generic').grid(row=3, column=1)

    def create_entry(self):
        self.id_var = tk.StringVar()
        self.id_entry = tk.Entry(self, textvariable=self.id_var)
        self.id_entry.grid(row=7, column=1)

    def create_buttons(self):
        self.add_button = tk.Button(self, text='Add Componenent', command=self.add_component)
        self.add_button.grid(row=8, column=1)
        self.delete_button = tk.Button(self, text='Delete Component', command=self.delete_component)
        self.delete_button.grid(row=9, column=1)

    def create_treeview(self):
        self.component_tree = ttk.Treeview(self)
        self.component_tree.grid(row=0, column=5, rowspan=20, columnspan=5)
        self.component_tree.bind("<Button-1>", self.on_treeview_click)

    def add_component(self):
        component_type = self.component_var.get()
        component_id = self.id_var.get()

        if not all([component_type, component_id]):
            messagebox.showerror("Missing Data", "All fields must be filled")
            return

        if component_id in self.components:
            messagebox.showerror("Duplicate ID", f"A component with ID {component_id} already exists")
            return

        self.components[component_id] = {'type': component_type}
        self.update_component_tree(component_id)
        self.component_order.append(component_id)

        messagebox.showinfo("Success", f"Added {component_type} with ID {component_id} to the project")

    def update_component_tree(self, component_id):
        selected_item = self.component_tree.focus()
        if selected_item:
            self.component_tree.insert(selected_item, 'end', component_id, text=component_id)
        elif self.component_order:
            self.component_tree.insert(self.component_order[-1], 'end', component_id, text=component_id)
        else:
            self.component_tree.insert('', 'end', component_id, text=component_id)

    def delete_component(self):
        selected_item = self.component_tree.focus()
        if selected_item:
            self.component_tree.delete(selected_item)
            self.component_order.remove(selected_item)
            del self.components[selected_item]

    def on_treeview_click(self, event):
        selected_item = self.component_tree.focus()  # get selected item
        if selected_item:
            self.id_var.set(selected_item)
