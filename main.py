import tkinter as tk
from gui.gui import QRCodeGUI

if __name__ == '__main__':
    root = tk.Tk()
    app = QRCodeGUI(root)
    root.mainloop()