# flag_checker_gui.py

import tkinter as tk
import hashlib


CORRECT_FLAG_HASH = "e3d44c721bf2ee74668ae917587907d328f327e8140e5168737f4486d9971ee9" # Example hash for "flag{example_flag}"

def check_flag(user_input):
    user_input = user_input.strip()
    user_input_hash = hashlib.sha256(user_input.encode()).hexdigest()
    
    if user_input_hash == CORRECT_FLAG_HASH:
        result_label.config(text="✅ Correct! Well done!", fg="green")
    else:
        result_label.config(text="❌ Incorrect flag. Try again!", fg="red")

# --- GUI Setup ---
root = tk.Tk()
root.title("Skills of Cybersecurity - Flag Checker")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

title_label = tk.Label(frame, text="Enter your flag guess:", font=("Arial", 14))
title_label.pack(pady=10)

flag_entry = tk.Entry(frame, width=40)
flag_entry.pack(pady=5)

submit_button = tk.Button(frame, text="Check Flag", command=lambda: check_flag(flag_entry.get()))
submit_button.pack(pady=10)

result_label = tk.Label(frame, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
