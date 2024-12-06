import tkinter as tk
from tkinter import messagebox

class Interfaced:
    def __init__(self, root, Title, Geometry, Description):
        self.root = root
        self.Title = Title
        self.Geometry = Geometry
        self.Description = Description
        self.root.title(Title)
        self.root.geometry(Geometry)
        
        # Label to display description
        self.label = tk.Label(root, text=Description)
        self.label.pack(pady=20)

        # Button to choose file location
        self.button = tk.Button(root, text="Choice file location", font=("Arial", 14), command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        # Action when button is clicked
        messagebox.showinfo("Button Clicked", "You clicked the button!")

    def create_button(self):
        # This method can be used for other button-related actions if needed
        print(self.Title)

    def run(self):
        # Start the main event loop
        self.root.mainloop()
