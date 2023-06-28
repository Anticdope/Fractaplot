import tkinter as tk
from ComponentManager import ComponentManagerPage
from ProjectManager import ProjectManagerPage
from MenuBar import MenuBar

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setup_window()
        self.create_menu_bar()
        self.create_frames()

    def setup_window(self):
        """Setup the main window."""
        self.title("FractaPlot Pro AC")
        self.geometry("800x600")

    def create_menu_bar(self):
        """Create the menu bar for the application."""
        self.menu_bar = MenuBar(self)
        self.config(menu=self.menu_bar)

    def create_frames(self):
        """Create and grid the available frames."""
        self.frames = {}
        for Frame in (ProjectManagerPage, ComponentManagerPage):
            frame = Frame(self)
            self.frames[Frame] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the default frame
        self.show_frame(ProjectManagerPage)

    def show_frame(self, frame_class):
        """Raise a frame to the top of the window."""
        frame = self.frames[frame_class]
        frame.tkraise()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
