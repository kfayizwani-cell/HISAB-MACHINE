import customtkinter as ctk


# Setup UI theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("350x500")
app.title("Hisab Machine")

app.resizable(False, False)

# Display Entry
display = ctk.CTkEntry(app,
                       width=300,
                       height=80,
                       corner_radius=20,
                       font=("Arial", 32),
                       justify="right")
display.pack(pady=20)


# Functionality
def add_value(value):
    current = display.get()
    display.delete(0, "end")
    display.insert(0, current + value)

def clear():
    display.delete(0, "end")

def evaluate():
    try:
        result = eval(display.get())
        display.delete(0, "end")
        display.insert(0, str(result))
    except:
        display.delete(0, "end")
        display.insert(0, "Error")


# Button Frame
frame = ctk.CTkFrame(app, width=320, height=350, corner_radius=25)
frame.pack(pady=10)

# Button style
btn_opts = {
    "width": 70,
    "height": 60,
    "corner_radius": 20,
    "font": ("Arial", 30)
}

# Layout of buttons
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
]

for (text, r, c) in buttons:
    if text == "=":
        btn = ctk.CTkButton(frame, text=text, fg_color="#2ecc71",
                            hover_color="#27ae60", **btn_opts,
                            command=evaluate)
    elif text in "+-*/":
        btn = ctk.CTkButton(frame, text=text, fg_color="#3498db",
                            hover_color="#2980b9", **btn_opts,
                            command=lambda t=text: add_value(t))
    else:
        btn = ctk.CTkButton(frame, text=text, fg_color="#ecf0f1",
                            text_color="black",
                            hover_color="#bdc3c7", **btn_opts,
                            command=lambda t=text: add_value(t))

    btn.grid(row=r, column=c, padx=8, pady=8)

# Clear button
clear_btn = ctk.CTkButton(app, text="CLEAR", fg_color="#e74c3c",
                          hover_color="#c0392b",
                          corner_radius=20,
                          width=300, height=55,
                          font=("Arial", 22),
                          command=clear)
clear_btn.pack(pady=10)

app.mainloop()
