# import os

# folder_path=r'D:\Automate Testing\Renaming Files'

# files=os.listdir(folder_path)

# for file_name in files:
#     if file_name.endswith(".txt"):
#         new_name="new_"+file_name
#         old_file=os.path.join(folder_path,file_name)
#         new_file=os.path.join(folder_path,new_name)
        
#         os.rename(old_file,new_file)
#         print(f"Rename: {file_name}->{new_name}")
        
import os
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, messagebox

# Function to rename files
def rename_files():
    folder_path = folder_path_var.get()
    prefix = prefix_var.get()
    suffix = suffix_var.get()
    
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder.")
        return
    
    if not prefix and not suffix:
        messagebox.showerror("Error", "Please provide a prefix or suffix.")
        return
    
    try:
        files = os.listdir(folder_path)
        renamed_count = 0
        
        for file_name in files:
            # Get the full path of the file
            old_file = os.path.join(folder_path, file_name)
            
            # Ignore directories
            if os.path.isdir(old_file):
                continue
            
            # Create new file name
            file_base, file_ext = os.path.splitext(file_name)
            new_name = f"{prefix}{file_base}{suffix}{file_ext}"
            new_file = os.path.join(folder_path, new_name)
            
            # Rename the file
            os.rename(old_file, new_file)
            renamed_count += 1
        
        # Show success message
        messagebox.showinfo("Success", f"Renamed {renamed_count} files successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to select folder
def select_folder():
    folder = filedialog.askdirectory()
    folder_path_var.set(folder)

# Create main GUI window
root = Tk()
root.title("File Renaming Tool")

# Variables for user input
folder_path_var = StringVar()
prefix_var = StringVar()
suffix_var = StringVar()

# GUI Layout
Label(root, text="Folder Path:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
Entry(root, textvariable=folder_path_var, width=40).grid(row=0, column=1, padx=10, pady=10)
Button(root, text="Browse", command=select_folder).grid(row=0, column=2, padx=10, pady=10)

Label(root, text="Prefix:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
Entry(root, textvariable=prefix_var, width=40).grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Suffix:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
Entry(root, textvariable=suffix_var, width=40).grid(row=2, column=1, padx=10, pady=10)

Button(root, text="Rename Files", command=rename_files, bg="green", fg="white").grid(row=3, column=1, pady=20)

# Start the GUI event loop
root.mainloop()
