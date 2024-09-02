import customtkinter as ctk
from pyperclip import copy

duping_times = 0

name = "text repeater"
output_options = ["print to terminal", "copy to clipboard", "print to terminal and copy to clipboard"]


def slider_changed(slider_value):
    global duping_times
    duping_times = int(slider_value)
    iterations_entry.configure(placeholder_text=str(duping_times))


def button_pressed():
    out_val = ""
    if check_box.get():
        for _ in range(duping_times):
            out_val += f"{text_entry.get()}\n"
    else:
        out_val = text_entry.get() * int(duping_times)
    if optionMenu_var.get() in output_options:
        print(out_val)
        print("\n\n")
    if optionMenu_var.get() == "copy to clipboard" or optionMenu_var.get() == "print to terminal and copy to clipboard":
        copy(out_val)


app = ctk.CTk()
# app.geometry("500x500")
app.title(name)
app.resizable(False, False)

ctk.set_default_color_theme("green")
ctk.set_appearance_mode("System")

frame = ctk.CTkFrame(master=app)
frame.pack(padx=10, pady=12, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text=name)
label.pack(padx=12, pady=10)

iterations_entry = ctk.CTkEntry(master=frame, placeholder_text="1")
iterations_entry.pack(padx=6, pady=10)

slider = ctk.CTkSlider(master=frame, from_=1, to=1_000, command=slider_changed)
slider.pack(padx=12, pady=10)
slider.set(0)

text_entry = ctk.CTkEntry(master=frame, placeholder_text="enter the text to get repeated")
text_entry.pack(padx=12, pady=10)

optionMenu_var = ctk.StringVar(value="Select output")
optionMenu = ctk.CTkOptionMenu(
    master=frame,
    values=output_options,
    variable=optionMenu_var
)
optionMenu.pack(padx=12, pady=10)
optionMenu.set("select output")

check_box_var = ctk.BooleanVar(value=False)
check_box = ctk.CTkCheckBox(master=frame, text="new line after every repeat", variable=check_box_var, onvalue=True,
                            offvalue=False)
check_box.pack(padx=12, pady=10)

button = ctk.CTkButton(master=frame, command=button_pressed, text="repeat the text!!!")
button.pack(padx=12, pady=10)

app.mainloop()

