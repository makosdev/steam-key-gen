import random
import string
import tkinter as tk

def generate_key():
    characters = string.ascii_uppercase + string.digits
    new_key = ''.join(random.choice(characters) for _ in range(17))
    return '-'.join([new_key[:5], new_key[5:11], new_key[11:]])

def generate_and_display_keys():
    keys = []
    for _ in range(10):
        key = generate_key()
        keys.append(key)

    print("Keys generated successfully!")
    print("Generated Keys:")
    print("\n".join(keys))

def generate_keys_gui():
    window = tk.Tk()
    window.title("Key Generator")
    window.geometry("300x100")

    label = tk.Label(window, text="Click the button to generate keys.")
    label.pack(pady=10)

    button = tk.Button(window, text="Generate Keys", command=generate_and_display_keys)
    button.pack()

    window.mainloop()

generate_keys_gui()
