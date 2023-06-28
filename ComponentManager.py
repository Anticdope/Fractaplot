import tkinter as tk
from tkinter import ttk
from DatabaseManager import DatabaseManager

class ComponentManagerPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.db_manager = DatabaseManager('FV-Components.db')
        self.create_widgets()

    def create_widgets(self):
        self.create_dropdown()
        self.create_field_frame()

    def create_dropdown(self):
        self.component_var = tk.StringVar()
        self.component_dropdown = ttk.Combobox(self, textvariable=self.component_var)
        self.component_dropdown['values'] = self.db_manager.get_component_types()
        self.component_dropdown.bind('<<ComboboxSelected>>', self.generate_input_fields)
        self.component_dropdown.grid(row=0, column=0, sticky='ew')

    def create_field_frame(self):
        self.input_field_frame = tk.Frame(self)
        self.input_field_frame.grid(row=1, column=0, columnspan=2, sticky='ew')

    def generate_input_fields(self):
        # Clear any previous input fields
        for widget in self.input_field_frame.winfo_children():
            widget.destroy()

        # Fetch the selected component type
        component_type = self.component_var.get()

        # Fetch the column names for the selected component type
        columns = self.db_manager.get_columns(component_type)

        # Generate an input field for each column
        for i, column in enumerate(columns, start=1):
            # Add a label
            label = tk.Label(self.input_field_frame, text=column)
            label.grid(row=i, column=0, sticky='e', padx=(10, 0), pady=(10, 0))  # add left padding to label

            # Add an entry field
            entry = tk.Entry(self.input_field_frame, width=30)  # set consistent width for entry field
            entry.grid(row=i, column=1, sticky='w', padx=(0, 10), pady=(10, 0))  # add right padding to entry field

        # Add the 'Add' button
        add_button = tk.Button(self.input_field_frame, text='Add', command=self.add_component)
        add_button.grid(row=i+1, column=0, columnspan=2, pady=(20, 0))  # add top padding to button

        # Delete component button
        delete_button = tk.Button(self.input_field_frame, text='Delete', command=self.delete_component)
        delete_button.grid(row=i+2, column=0, columnspan=2, pady=(10, 0))


    def clear_previous_fields(self):
        for widget in self.input_field_frame.winfo_children():
            widget.destroy()

    def create_fields(self, columns):
        for i, column in enumerate(columns, start=1):
            self.create_label(column, i)
            self.create_entry(i)

    def create_label(self, column, i):
        label = tk.Label(self.input_field_frame, text=column)
        label.grid(row=i, column=0, sticky='e', padx=(10, 0), pady=(10, 0))

    def create_entry(self, i):
        entry = tk.Entry(self.input_field_frame, width=30)
        entry.grid(row=i, column=1, sticky='w', padx=(0, 10), pady=(10, 0))

    def create_buttons(self):
        add_button = tk.Button(self.input_field_frame, text='Add', command=self.add_component)
        add_button.grid(row=i+1, column=0, columnspan=2, pady=(20, 0))
        delete_button = tk.Button(self.input_field_frame, text='Delete', command=self.delete_component)
        delete_button.grid(row=i+2, column=0, columnspan=2, pady=(10, 0))

    def add_component(self):
        pass

    def search_component(self):
        pass

    def delete_component(self):
        pass
