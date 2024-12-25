import os
from tkinter import Tk, Frame, Label, Listbox, Scrollbar, filedialog
from tkinter.messagebox import showinfo

def list_files():
    # Clear the listbox
    file_listbox.delete(0, "end")

    # Get all files in the directory
    path = r"D:\NX_BACKWORK\Database_File\SMT_SOP"
    file_extensions = (".ppt", ".pptx", ".xls", ".xlsx")
    
    if os.path.exists(path):
        files = [f for f in os.listdir(path) if f.endswith(file_extensions)]
        if files:
            for file in files:
                file_listbox.insert("end", file)
        else:
            showinfo("No Files", "No PowerPoint or Excel files found in the directory.")
    else:
        showinfo("Error", f"The directory {path} does not exist.")

def open_file():
    selected = file_listbox.get(file_listbox.curselection())
    file_path = os.path.join(r"D:\NX_BACKWORK\Database_File\SMT_SOP", selected)
    os.startfile(file_path)

# Create the UI
root = Tk()
root.title("Digital Library Manager")
root.geometry("500x400")

# Header
header_frame = Frame(root)
header_frame.pack(pady=10)
header_label = Label(header_frame, text="Digital Library Manager", font=("Arial", 16))
header_label.pack()

# Listbox with scrollbar
list_frame = Frame(root)
list_frame.pack(pady=10, fill="both", expand=True)

scrollbar = Scrollbar(list_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

file_listbox = Listbox(list_frame, yscrollcommand=scrollbar.set, font=("Arial", 12), height=15)
file_listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=file_listbox.yview)

# Buttons
btn_frame = Frame(root)
btn_frame.pack(pady=10)

list_btn = Label(btn_frame, text="List Files", font=("Arial", 12), bg="lightblue", width=12, cursor="hand2")
list_btn.pack(side="left", padx=5)
list_btn.bind("<Button-1>", lambda e: list_files())

open_btn = Label(btn_frame, text="Open File", font=("Arial", 12), bg="lightgreen", width=12, cursor="hand2")
open_btn.pack(side="left", padx=5)
open_btn.bind("<Button-1>", lambda e: open_file())

# Start the application
root.mainloop()