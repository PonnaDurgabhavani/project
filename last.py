import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

# ================= Password Generation Functions =================

def generate_random_password(length=12):
    if length < 6:
        length = 6
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice("!@#$%^&*()")
    others = random.choices(string.ascii_letters + string.digits + "!@#$%^&*()", k=length - 4)
    password = list(lower + upper + digit + symbol + ''.join(others))
    random.shuffle(password)
    return ''.join(password)

def generate_memorable_password(word_count, capitalize=False, use_full_words=True):
    base_words = ["apple", "banana", "cherry", "delta", "echo", "forest", "giant", "honey", "island", "jungle"]
    
    selected = random.sample(base_words, word_count)
    
    if not use_full_words:
        selected = [word[:random.randint(3, 4)] for word in selected]  # Crop to 3–4 letters

    if capitalize:
        selected = [word.capitalize() for word in selected]
    
    return '-'.join(selected)





# ================= GUI =================

def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

def fill_generated_password():
    def choose(option):
        for widget in extra_frame.winfo_children():
            widget.destroy()

        if option == "Random":
            show_info("Password will include uppercase, lowercase, digits, and symbols.")

            # This will show password in popup instead of closing it
            result_var = tk.StringVar()

            def generate_and_show():
                pwd = generate_random_password(length_var.get())
                result_var.set(pwd)

            # Optional: Fill it into the main registration form too
                password_var.set(pwd)
                if show_password_var.get():
                    password_entry.config(show='')
                else:
                    password_entry.config(show='*')
                
 
            # Password length slider
            tk.Label(extra_frame, text="Select Password Length:", font=("Arial", 10)).pack(anchor='w')
            length_var = tk.IntVar(value=12)
            length_slider = tk.Scale(extra_frame, from_=8, to=20, orient='horizontal',
                         variable=length_var, showvalue=True)
            length_slider.pack(anchor='w', pady=(0, 5))
            ttk.Separator(popup, orient='horizontal').pack(fill='x', padx=10, pady=5)

            # Button to generate
            ttk.Button(extra_frame, text="Generate", command=generate_and_show).pack(anchor='w', pady=(5, 5))

            # Display generated password
            tk.Label(extra_frame, text="Generated Password:", font=("Arial", 10)).pack(anchor='w')
            tk.Entry(extra_frame, textvariable=result_var, font=("Arial", 10), width=25, state='readonly').pack(anchor='w')
            # ⬇️ Add the buttons right after the Entry field
            buttons_frame = tk.Frame(extra_frame)
            buttons_frame.pack(anchor='w', pady=5)

            # 📋 Copy password
            def copy_to_clipboard():
                popup.clipboard_clear()
                popup.clipboard_append(result_var.get())
                popup.update()
                messagebox.showinfo("Copied", "Password copied to clipboard!")


            ttk.Button(buttons_frame, text="Copy Password", command=copy_to_clipboard).pack(side='left', padx=5)
            def update_password(length):
                pwd = generate_random_password(int(float(length)))
                result_var.set(pwd)
                password_var.set(pwd)
                password_entry.config(show='' if show_password_var.get() else '*')

        
            # 🔁 Refresh password
            def refresh_password():
                update_password(length_var.get())

            ttk.Button(buttons_frame, text="Refresh password", command=refresh_password).pack(side='left', padx=5)

            # Trigger first password generation
            generate_random_password(length_var.get())


        elif option == "Memorable":
            memorable_length_var = tk.IntVar(value=3)
            capitalize_var = tk.BooleanVar(value=False)
            use_full_words_var = tk.BooleanVar(value=True)


            result_var = tk.StringVar()  # <-- Move this here first!

            def update_memorable_password(word_count):
                   pwd = generate_memorable_password(
                                                      int(float(word_count)),
                                                      capitalize=capitalize_var.get(),
                                                      use_full_words=use_full_words_var.get()
                                                    )

                   result_var.set(pwd)
                   password_var.set(pwd)
                   password_entry.config(show='' if show_password_var.get() else '*')

            

            # Now it's safe to use result_var in widgets and commands


            tk.Label(extra_frame, text="Select Words Length:", font=("Arial", 10)).pack(anchor='w')
            memorable_length_var = tk.IntVar(value=3)
            length_slider = tk.Scale(extra_frame, from_=3, to=9, orient='horizontal',
                         variable=memorable_length_var, showvalue=True)
            length_slider.pack(anchor='w', pady=(0, 5))
            

            
            

            tk.Checkbutton(
                               extra_frame,
                               text="Capitalize first letter of each word",
                               variable=capitalize_var,
                               command=lambda: update_memorable_password(memorable_length_var.get())
                          ).pack(anchor='w')
            tk.Checkbutton(
                              extra_frame,
                              text="Use full words only",
                              variable=use_full_words_var,
                              command=lambda: update_memorable_password(memorable_length_var.get())
                          ).pack(anchor='w')
            ttk.Separator(extra_frame, orient='horizontal').pack(fill='x', padx=10, pady=5)
            


            
            # Display generated password
            tk.Label(extra_frame, text="Generated Password:", font=("Arial", 10)).pack(anchor='w')
            tk.Entry(extra_frame, textvariable=result_var, font=("Arial", 10), width=25, state='readonly').pack(anchor='w')

            # ⬇️ Add the buttons right after the Entry field
            buttons_frame = tk.Frame(extra_frame)
            buttons_frame.pack(anchor='w', pady=5)

            # 📋 Copy password
            def copy_to_clipboard():
                popup.clipboard_clear()
                popup.clipboard_append(result_var.get())
                popup.update()
                messagebox.showinfo("Copied", "Password copied to clipboard!")


            ttk.Button(buttons_frame, text="Copy Password", command=copy_to_clipboard).pack(side='left', padx=5)
            def update_memorable_password(word_count):
                   pwd = generate_memorable_password(
                                                      int(float(word_count)),
                                                      capitalize=capitalize_var.get(),
                                                      use_full_words=use_full_words_var.get()
                                                    )

                   result_var.set(pwd)
                   password_var.set(pwd)
                   password_entry.config(show='' if show_password_var.get() else '*')

            ttk.Button(
                        buttons_frame,
                        text="Refresh",
                        command=lambda: update_memorable_password(memorable_length_var.get())
                        ).pack(side='left', padx=5)


            update_memorable_password(memorable_length_var.get())

        

    # Popup Window
    popup = tk.Toplevel(root)
    popup.title("Strong-Secure-Password")
    popup.geometry("360x280")
    
    popup.grab_set()

    tk.Label(popup, text="Choose Password Type:", font=("Arial", 12)).pack(anchor='w', padx=10, pady=(10, 0))
    ttk.Separator(popup, orient='horizontal').pack(fill='x', padx=10, pady=5)

    # Info label
    info_frame = tk.Frame(popup)
    info_frame.pack(anchor='w', padx=10)
    info_label = tk.Label(info_frame, text="", fg="gray", font=("Arial", 9))
    info_label.pack(anchor='w')

    def show_info(msg):
        info_label.config(text=msg)

    # Buttons
    button_frame = tk.Frame(popup)
    button_frame.pack(pady=10)

    ttk.Button(button_frame, text="🔐 Random Password", command=lambda: choose("Random")).pack(side='left', padx=5)
    
    ttk.Button(button_frame, text="🧠 Memorable Password", command=lambda: choose("Memorable")).pack(side='left', padx=5)

    
    

    # Dynamic frame for extra controls (slider, etc.)
    extra_frame = tk.Frame(popup)
    extra_frame.pack(padx=10, pady=10, fill='x')


   


    




def validate_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*()" for c in password)
    return has_upper and has_lower and has_digit and has_symbol

def register_user():
    name = name_var.get()
    email = email_var.get()
    password = password_var.get()

    if not name or not email or not password:
        messagebox.showerror("Error", "All fields are required.")
        return

    if not validate_password(password):
        messagebox.showerror("Error", "Password must include uppercase, lowercase, digit, and symbol.")
        return

    messagebox.showinfo("Success",  f"Registration successful!\nName: {name}\nEmail: {email}\nPassword: {password}")

# ================= Window =================

root = tk.Tk()
root.title("Registration Form with Password Generator")
root.geometry("450x400")

tk.Label(root, text="User Registration Foem", font=("Calibri", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

# Name
tk.Label(frame, text="* Name:").grid(row=0, column=0, sticky='e', pady=5)
name_var = tk.StringVar()
ttk.Entry(frame, textvariable=name_var, width=30).grid(row=0, column=1)

# Email
tk.Label(frame, text="* Email:").grid(row=1, column=0, sticky='e', pady=5)
email_var = tk.StringVar()
ttk.Entry(frame, textvariable=email_var, width=30).grid(row=1, column=1)

# Password
tk.Label(frame, text="* Password:").grid(row=2, column=0, sticky='e', pady=5)
password_var = tk.StringVar()
password_entry = ttk.Entry(frame, textvariable=password_var, width=30, show='*')
password_entry.grid(row=2, column=1)

# Show Password
show_password_var = tk.BooleanVar()
show_password_check = ttk.Checkbutton(frame, text="Show Password", variable=show_password_var, command=toggle_password_visibility)
show_password_check.grid(row=3, column=1, sticky='w')


# Confirm Password
tk.Label(frame, text="*Confirm Password:").grid(row=4, column=0, sticky='e', pady=5)
confirm_password_var = tk.StringVar()
confirm_password_entry = ttk.Entry(frame, textvariable=password_var, width=30, show='*')
confirm_password_entry.grid(row=4, column=1)
# Generate Password Button
ttk.Button(frame, text="Generate Password", command=fill_generated_password)\
    .grid(row=5, column=1, sticky='w', pady=5)



# Register Button
ttk.Button(root, text="Register", command=register_user).pack(pady=10)


root.mainloop()


