import customtkinter as customtk
from pyperclip import copy


duping_times = 0
def slider_changed(slider_value):
    global duping_times
    duping_times = int(slider_value)
    slider_label.configure(text=duping_times)


def button_presed():
    outval = ""
    if check_box.get():
        for _ in range(duping_times):
            outval += f"{entry.get()}\n"
    else:
          outval = entry.get() * int(duping_times)
    if optionmenu_var.get() == "print to terminal" or optionmenu_var.get() == "print to terminal and copy to clipboard":
          print(outval)
          print("\n\n")
    if optionmenu_var.get() == "copy to clipboard" or optionmenu_var.get() == "print to terminal and copy to clipboard":
          copy(outval)    

app = customtk.CTk()
# app.geometry("500x500")
app.title("app")
# app.resizable(False, False)

customtk.set_default_color_theme("green")
customtk.set_appearance_mode("System")

frame = customtk.CTkFrame(master=app)
frame.pack(padx=10, pady=12, fill="both", expand=True)

label = customtk.CTkLabel(master=frame, text="text duper")
label.pack(padx=12, pady=10)

slider_label = customtk.CTkLabel(master=frame, text=1)
slider_label.pack(padx=12, pady=10)

slider = customtk.CTkSlider(master=frame, from_=1, to=1_000, command=slider_changed)
slider.pack(padx=12, pady=10)
slider.set(0)

entry = customtk.CTkEntry(master=frame, placeholder_text="enter the text to get duped")
entry.pack(padx=12, pady=10)

optionmenu_var = customtk.StringVar(value="Select output")
optionmenu = customtk.CTkOptionMenu(
    master=frame, 
    values=("print to terminal", "copy to clipboard", "print to terminal and copy to clipboard"),
    variable=optionmenu_var
)
optionmenu.pack(padx=12, pady=10)
optionmenu.set("select output")

check_box_var = customtk.BooleanVar(value=False)
check_box = customtk.CTkCheckBox(master=frame, text="new line after repeat", variable=check_box_var, onvalue=True, offvalue=False)
check_box.pack(padx=12, pady=10)

button = customtk.CTkButton(master=frame, command=button_presed, text="dupe")
button.pack(padx=12, pady=10)

app.mainloop()