import tkinter as tk
from tkinter import colorchooser, messagebox
import qrcode  
from qr_setting.qr_generator import generate_qr_code

class QRCodeGUI:
    def __init__(self, master):
        self.master = master
        master.title("QR Code Generator")
        
        # 📝 URL入力エリア
        tk.Label(master, text="URL:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.insert(0, "https://www.sample.com")
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)

        # 📝 出力ファイル名を指定
        tk.Label(master, text="QRコードのファイル名:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.filename_entry = tk.Entry(master, width=50)
        self.filename_entry.insert(0, "qrcode.png")
        self.filename_entry.grid(row=1, column=1, padx=5, pady=5)

        # 🎨 QRコード自体の色を指定
        tk.Label(master, text="QRコードの色を指定:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.fill_color = "#000000"  # 初期値：黒
        self.fill_color_button = tk.Button(master, text=self.fill_color, bg=self.fill_color, command=self.choose_fill_color, width=10)
        self.fill_color_button.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # 🎨 背景色を指定
        tk.Label(master, text="背景色を指定:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.back_color = "#ffffff"  # 初期値：白
        self.back_color_button = tk.Button(master, text=self.back_color, bg=self.back_color, command=self.choose_back_color, width=10)
        self.back_color_button.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # 🚀 QRコード生成ボタン
        self.generate_button = tk.Button(master, text="Generate QR Code", command=self.generate_qr)
        self.generate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    def choose_fill_color(self):
        color_code = colorchooser.askcolor(title="Choose fill color", initialcolor=self.fill_color)
        if color_code[1]:
            self.fill_color = color_code[1]
            self.fill_color_button.config(text=self.fill_color, bg=self.fill_color)

    def choose_back_color(self):
        color_code = colorchooser.askcolor(title="Choose back color", initialcolor=self.back_color)
        if color_code[1]:
            self.back_color = color_code[1]
            self.back_color_button.config(text=self.back_color, bg=self.back_color)

    def generate_qr(self):
        url = self.url_entry.get()
        filename = self.filename_entry.get()
        if not url or not filename:
            messagebox.showerror("Input Error", "URLと出力ファイル名は必須です。")
            return

        img = generate_qr_code(
            url, 
            self.fill_color, 
            self.back_color, 
            version=1, 
            error_correction=qrcode.constants.ERROR_CORRECT_L, 
            box_size=10, 
            border=4
        )
        try:
            img.save(filename)
            messagebox.showinfo("Success", f"QRコードを {filename} に保存しました。")
        except Exception as e:
            messagebox.showerror("Save Error", f"QRコードの保存に失敗しました: {e}")

if __name__ == '__main__':
    root = tk.Tk()
    app = QRCodeGUI(root)
    root.mainloop()
