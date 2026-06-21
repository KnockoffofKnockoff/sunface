import tkinter as tk
from objects import Color

root = tk.Tk()
root.title("HOI4 Modding")

create_country = tk.Button(root, text="Create Country")
create_country.grid(row=0, column=0, padx=10, pady=10)

create_focus_tree = tk.Button(root, text="Create Focus Tree")
create_focus_tree.grid(row=0, column=1, padx=10, pady=10)

print(Color(1, 2, 3))

root.mainloop()
