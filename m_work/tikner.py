import tkinter as tk


def register():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # Ma'lumotlarni serverga yuborish va foydalanuvchi ro'yxatdan o'tkazilishi


root = tk.Tk()
root.title("Registratsiya sahifasi")

# Foydalanuvchi ismi uchun maydoncha
username_label = tk.Label(root, text="Foydalanuvchi ismi:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Elektron pochta manzili uchun maydoncha
email_label = tk.Label(root, text="Elektron pochta manzili:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Parol uchun maydoncha
password_label = tk.Label(root, text="Parol:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Registratsiya tugmasi
register_button = tk.Button(root, text="Ro'yxatdan o'tish", command=register)
register_button.pack()

root.mainloop()
