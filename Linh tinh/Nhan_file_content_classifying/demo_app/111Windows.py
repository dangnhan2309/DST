from Tkinter_windows.tkinter_testing import Interfaced
import tkinter as tk
def main():
    root = tk.Tk()
    app = Interfaced(root, "My Application", "300x200", "This is a description of the app.")
    app.run()
main() 