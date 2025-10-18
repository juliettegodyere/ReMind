import tkinter as tk

root = tk.Tk()
root.title("ReMind Test")
root.geometry("300x150")

label = tk.Label(root, text="Tkinter is working!", font=("Arial", 14))
label.pack(pady=20)

root.mainloop()

