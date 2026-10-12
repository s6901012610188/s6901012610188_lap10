import tkinter as tk
from tkinter import messagebox


class TextAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Text Analyzer")
        self.root.geometry("420x340")
        self.root.resizable(False, False)

        # ช่องรับข้อความ
        tk.Label(root, text="ข้อความ:", font=("Arial", 12)).pack(pady=(15, 3))
        self.text_entry = tk.Entry(root, font=("Arial", 13), width=30, justify="center")
        self.text_entry.pack(pady=3)

        # ช่องรับตัวอักษรที่ต้องการค้นหา (สั้นๆ)
        tk.Label(root, text="ตัวอักษรที่ต้องการนับ:", font=("Arial", 12)).pack(pady=(10, 3))
        self.char_entry = tk.Entry(root, font=("Arial", 13), width=5, justify="center")
        self.char_entry.pack(pady=3)

        # ปุ่มต่างๆ
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=15)

        tk.Button(
            btn_frame, text="Count Character", width=16, command=self.show_count_char
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            btn_frame, text="Count Vowels", width=16, command=self.show_count_vowels
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            btn_frame, text="Check Palindrome", width=34, command=self.show_palindrome
        ).grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Label แสดงผลลัพธ์
        self.result_label = tk.Label(
            root, text="ผลลัพธ์จะแสดงที่นี่", font=("Arial", 13, "bold"),
            wraplength=380, fg="blue"
        )
        self.result_label.pack(pady=10)

    # ---------- ฟังก์ชันวิเคราะห์ข้อความ (ใช้เมธอดของ String) ----------
    def count_character(self, text, char):
        """นับจำนวนตัวอักษรที่ระบุ (ไม่สนใจตัวพิมพ์เล็ก/ใหญ่)"""
        return text.lower().count(char.lower())

    def count_vowels(self, text):
        """นับจำนวนสระ a, e, i, o, u ทั้งหมด"""
        total = 0
        for ch in text.lower():
            if ch in "aeiou":
                total += 1
        return total

    def is_palindrome(self, text):
        """ตรวจสอบ Palindrome (ตัดช่องว่างและไม่สนใจตัวพิมพ์เล็ก/ใหญ่)"""
        cleaned = text.replace(" ", "").lower()
        return cleaned == cleaned[::-1]

    # ---------- ฟังก์ชันที่ผูกกับปุ่ม ----------
    def get_text(self):
        text = self.text_entry.get().strip()
        if text == "":
            messagebox.showwarning("คำเตือน", "กรุณากรอกข้อความก่อน")
            return None
        return text

    def show_count_char(self):
        text = self.get_text()
        if text is None:
            return
        char = self.char_entry.get()
        if len(char) != 1:
            messagebox.showwarning("คำเตือน", "กรุณากรอกตัวอักษรที่ต้องการนับ 1 ตัว")
            return
        n = self.count_character(text, char)
        self.result_label.config(text=f'ตัวอักษร "{char}" พบ {n} ครั้งใน "{text}"')

    def show_count_vowels(self):
        text = self.get_text()
        if text is None:
            return
        n = self.count_vowels(text)
        self.result_label.config(text=f'"{text}" มีสระ (a, e, i, o, u) ทั้งหมด {n} ตัว')

    def show_palindrome(self):
        text = self.get_text()
        if text is None:
            return
        if self.is_palindrome(text):
            self.result_label.config(text=f'"{text}" เป็น Palindrome')
        else:
            self.result_label.config(text=f'"{text}" ไม่เป็น Palindrome')


if __name__ == "__main__":
    root = tk.Tk()
    app = TextAnalyzerApp(root)
    root.mainloop()