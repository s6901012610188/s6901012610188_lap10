import tkinter as tk
from tkinter import messagebox


class TempConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Celsius to Fahrenheit Converter")
        self.root.geometry("360x220")
        self.root.resizable(False, False)

        # ข้อความกำกับช่องกรอก
        tk.Label(root, text="กรอกอุณหภูมิ (°C):", font=("Arial", 12)).pack(pady=(20, 5))

        # ช่องรับข้อมูล (Entry) สำหรับกรอกอุณหภูมิเป็นเซลเซียส
        self.entry = tk.Entry(root, font=("Arial", 14), justify="center", width=15)
        self.entry.pack(pady=5)
        self.entry.focus()

        # ปุ่ม Convert
        self.btn_convert = tk.Button(
            root, text="Convert", width=12, command=self.convert
        )
        self.btn_convert.pack(pady=10)

        # Label แสดงผลลัพธ์เป็นฟาเรนไฮต์
        self.result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=10)

        # กด Enter เพื่อแปลงค่าได้เช่นกัน
        self.root.bind("<Return>", lambda event: self.convert())

    def convert(self):
        text = self.entry.get().strip()
        try:
            celsius = float(text)
        except ValueError:
            # กรณีผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข
            messagebox.showwarning("คำเตือน", "กรุณากรอกเฉพาะตัวเลขเท่านั้น")
            self.result_label.config(text="")
            return

        fahrenheit = (celsius * 9 / 5) + 32
        self.result_label.config(text=f"{celsius:g} °C = {fahrenheit:.2f} °F")


if __name__ == "__main__":
    root = tk.Tk()
    app = TempConverterApp(root)
    root.mainloop()