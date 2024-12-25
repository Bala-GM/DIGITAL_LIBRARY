import os
from tkinter import Tk, Frame, Label, Listbox, Scrollbar
from tkinter.messagebox import showinfo

def list_files():
    # Clear the listbox
    file_listbox.delete(0, "end")

    # Supported file extensions
    file_extensions = (".ppt", ".pptx", ".xls", ".xlsx", ".pdf", ".txt", ".html", ".htm", ".doc", ".docx")
    
    # Directory path
    path = r"D:\NX_BACKWORK\Database_File\SMT_SOP"

    if os.path.exists(path):
        files = [f for f in os.listdir(path) if f.endswith(file_extensions)]
        if files:
            for file in files:
                file_listbox.insert("end", file)
        else:
            showinfo("No Files", "No supported files found in the directory.")
    else:
        showinfo("Error", f"The directory {path} does not exist.")

def open_file():
    try:
        selected = file_listbox.get(file_listbox.curselection())
        file_path = os.path.join(r"D:\NX_BACKWORK\Database_File\SMT_SOP", selected)
        os.startfile(file_path)
    except Exception as e:
        showinfo("Error", f"Unable to open file: {str(e)}")

# Create the UI
root = Tk()
root.title("Digital Library Manager")
root.geometry("600x500")
root.config(bg="black")

# Header
header_frame = Frame(root, bg="black")
header_frame.pack(pady=20)

header_label = Label(header_frame, text="Digital Library Manager", font=("Arial", 18, "bold"), bg="black", fg="green")
header_label.pack()

# Listbox with scrollbar
list_frame = Frame(root, bg="black")
list_frame.pack(pady=10, padx=50, fill="both", expand=True)

scrollbar = Scrollbar(list_frame, orient="vertical", bg="black", troughcolor="black", activebackground="green")
scrollbar.pack(side="right", fill="y")

file_listbox = Listbox(
    list_frame, yscrollcommand=scrollbar.set, font=("Arial", 12), height=15, bg="black", fg="green", selectbackground="green"
)
file_listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=file_listbox.yview)

# Buttons
btn_frame = Frame(root, bg="black")
btn_frame.pack(pady=20)

list_btn = Label(btn_frame, text="List Files", font=("Arial", 12, "bold"), bg="green", fg="black", width=15, cursor="hand2")
list_btn.pack(side="left", padx=10)
list_btn.bind("<Button-1>", lambda e: list_files())

open_btn = Label(btn_frame, text="Open File", font=("Arial", 12, "bold"), bg="green", fg="black", width=15, cursor="hand2")
open_btn.pack(side="left", padx=10)
open_btn.bind("<Button-1>", lambda e: open_file())

# Start the application
root.mainloop()