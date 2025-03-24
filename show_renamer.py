import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files():
    folder = filedialog.askdirectory(title="Select Folder with Episodes")
    if not folder:
        return
    show_name = show_name_entry.get().strip()
    season = season_entry.get().strip()
    if not show_name:
        messagebox.showerror("Input Error", "Please enter a show name.")
        return
    try:
        season_int = int(season)
    except ValueError:
        messagebox.showerror("Input Error", "Season must be an integer.")
        return
    files = sorted(os.listdir(folder))
    episode_number = 1
    for filename in files:
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1]
            new_name = f"{show_name} - S{season_int:02d}E{episode_number:02d}{ext}"
            new_path = os.path.join(folder, new_name)
            try:
                os.rename(file_path, new_path)
            except Exception as e:
                messagebox.showerror("Rename Error", f"Error renaming '{filename}': {e}")
                return
            episode_number += 1
    messagebox.showinfo("Success", "Files renamed successfully!")

root = tk.Tk()
root.title("TV Show Episode Renamer")
tk.Label(root, text="Show Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
show_name_entry = tk.Entry(root, width=30)
show_name_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Label(root, text="Season:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
season_entry = tk.Entry(root, width=30)
season_entry.grid(row=1, column=1, padx=5, pady=5)
rename_button = tk.Button(root, text="Select Folder & Rename", command=rename_files)
rename_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
root.mainloop()
