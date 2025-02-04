import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar

from main import FileOrganizer

organize = FileOrganizer()
# create the toplevel window
root = ttk.Window()
root.geometry("450x400")
root.title("File Organizer App")

def on_submit():
    src_folder = entry_src.get()
    if entry_dst.get():
        dst_folder = organize.check_dst_folder(entry_dst.get())# checking destination folder whether it is exist or not.
        organize.file_organizer(src_folder, dst_folder)
    

# validate source folder
ttk.Label(root, text="Enter Source Folder", font=("Helvetica bold", 15)).pack(padx=20, pady=20)
entry_src = StringVar()
src_dir = ttk.Entry(root, bootstyle="primary", textvariable = entry_src, width=40)
src_dir.pack(padx=10, pady=10)

# validate dst folder
entry_dst = StringVar()
ttk.Label(root,text="Enter Destination Folder", font=("Helvetica bold", 15)).pack(padx=20, pady=20)
dst_dir = ttk.Entry(root, bootstyle="primary", textvariable= entry_dst, width=40)
dst_dir.pack(padx=10, pady=10)


# Submit button
submit = ttk.Button(root, text="Submit", command=on_submit)
submit.pack(padx=10, pady=10)


root.mainloop()
