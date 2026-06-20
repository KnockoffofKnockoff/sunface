import tkinter as tk

root = tk.Tk()
root.title("HOI4 Modding")

btn_top_left = tk.Button(root, text="Create Country")
btn_top_left.grid(row=0, column=0, padx=10, pady=10)

btn_top_right = tk.Button(root, text="Create Focus Tree")
btn_top_right.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
