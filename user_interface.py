import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  
siemens_blue = "#0d0140"
siemens_green = "#009999"  # Siemens wincc website colors
siemens_white = "#FFFFFF"
def toggle_dropdown():
    if listbox.winfo_ismapped():
        listbox.pack_forget()  
    else:
        listbox.pack(pady=10)  

def update_selection(event):
    selected_choices = [listbox.get(idx) for idx in listbox.curselection()]
    selected_var.set(", ".join(selected_choices))

def select_all():
    listbox.selection_set(0, tk.END)  
    update_selection(None)  
root = tk.Tk()
root.title("Choice Describer")
root.configure(bg=siemens_blue)  
root.geometry("600x400")  

#  image
image = Image.open("siemens_image.png")  # the imsge "siemens_image.png" needs to be on he same location!!
image = image.resize((400, 200), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=image, bg=siemens_blue)
image_label.pack(pady=10)
siemens_label = tk.Label(root, text="Siemens", font=("Arial", 24, "bold"), bg=siemens_blue, fg=siemens_white)
siemens_label.pack(pady=10)
subtitle_label = tk.Label(root, text="Comparative Analysis of SCADA Systems", font=("Arial", 14), bg=siemens_blue, fg=siemens_white)
subtitle_label.pack(pady=10)
dropdown_label = tk.Label(root, text="Companies:", font=("Arial", 12), bg=siemens_blue, fg=siemens_white)
dropdown_label.pack(pady=10)
preset_companies = ["Siemens", 
    "Schneider Electric",
    "Rockwell Automation",
    "ABB",
    "Wonderware",
    "GE Digital",]
selected_var = tk.StringVar()
selected_var.set("") 
selected_label = tk.Label(root, textvariable=selected_var, font=("Arial", 12), bg=siemens_blue, fg=siemens_white)
selected_label.pack(pady=10)
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Arial", 12), bg=siemens_blue, selectbackground=siemens_green, height=len(preset_companies))
for company in preset_companies:
    listbox.insert(tk.END, company)
listbox.bind('<<ListboxSelect>>', update_selection)
dropdown_button = tk.Button(root, text="Select Companies", font=("Arial", 12), bg=siemens_green, fg=siemens_white, command=toggle_dropdown, relief=tk.FLAT)
dropdown_button.pack(pady=10)
select_all_button = tk.Button(root, text="Select All", font=("Arial", 12), bg=siemens_green, fg=siemens_white, command=select_all, relief=tk.FLAT)
select_all_button.pack(pady=10)
root.mainloop()
