import tkinter as tk


class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter App")
        self.root.geometry("320x240")
        self.root.resizable(False, False)

        self.count = 0

        # ข้อความแสดงตัวเลข (เริ่มต้นที่ 0)
        self.label = tk.Label(root, text=str(self.count), font=("Arial", 48, "bold"))
        self.label.pack(pady=25)

        frame = tk.Frame(root)
        frame.pack()

        # ปุ่ม Increase เพิ่มค่าครั้งละ 1
        self.btn_increase = tk.Button(
            frame, text="Increase", width=10, command=self.increase
        )
        self.btn_increase.grid(row=0, column=0, padx=5, pady=5)

        # ปุ่ม Decrease ลดค่าครั้งละ 1
        self.btn_decrease = tk.Button(
            frame, text="Decrease", width=10, command=self.decrease
        )
        self.btn_decrease.grid(row=0, column=1, padx=5, pady=5)

        # ปุ่ม Reset ตั้งค่ากลับเป็น 0
        self.btn_reset = tk.Button(
            root, text="Reset", width=22, command=self.reset
        )
        self.btn_reset.pack(pady=10)

    def update_label(self):
        self.label.config(text=str(self.count))

    def increase(self):
        self.count += 1
        self.update_label()

    def decrease(self):
        self.count -= 1
        self.update_label()

    def reset(self):
        self.count = 0
        self.update_label()


if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()