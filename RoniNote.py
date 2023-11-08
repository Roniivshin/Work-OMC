import tkinter as tk
import os
from tkinter import simpledialog

class MyGui:

    def __init__(self):
        # Create a frame to hold the buttons
        self.root = tk.Tk()
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.TOP, expand=True, anchor=tk.NE)  # Position the frame at the top right
        self.button = tk.Button(self.root, text="New", command=self.create_folder)
        self.button.pack(padx=5, pady=2, side=tk.RIGHT, anchor=tk.NW)
        self.first_button_list()
        self.textbox = tk.Text(self.root)
        self.textbox.pack(padx=5, pady=5)

        self.root.mainloop()

    def update_list(self):
        print(self.button_frame)
        folder_location = f"C:\\Users\\Roni\\PycharmProjects\\pythonProject1\\RoniNote\\"
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        directories = [d for d in os.listdir(folder_location) if os.path.isdir(os.path.join(folder_location, d))]
        for directory in directories:
            button = tk.Button(self.button_frame, text=directory, command=self.update_list)
            button.pack(padx=5, pady=2, side=tk.RIGHT, anchor=tk.NW)
        text_files = [f for f in os.listdir(folder_location) if
                      f.endswith(".txt") and os.path.isfile(os.path.join(folder_location, f))]
        for file in text_files:
            button = tk.Button(self.button_frame, text=file)
            button.pack(padx=5, pady=2, side=tk.RIGHT, anchor=tk.NW)
    def first_button_list(self):
        folder_location = "C:\\Users\\Roni\\PycharmProjects\\pythonProject1\\RoniNote"
        directories = [d for d in os.listdir(folder_location) if os.path.isdir(os.path.join(folder_location, d))]
        for directory in directories:
            button = tk.Button(self.button_frame, text=directory, command=self.update_list)
            button.pack(padx=5, pady=2, side=tk.RIGHT, anchor=tk.NW)
        text_files = [f for f in os.listdir(folder_location) if
                      f.endswith(".txt") and os.path.isfile(os.path.join(folder_location, f))]
        for file in text_files:
            button = tk.Button(self.button_frame, text=file)
            button.pack(padx=5, pady=2, side=tk.RIGHT, anchor=tk.NW)

    def create_folder(self):
        # Specify the directory where you want to create the new folder
        folder_location = "C:\\Users\\Roni\\PycharmProjects\\pythonProject1\\RoniNote"
        # Check if the directory location exists
        if os.path.exists(folder_location):
            # Generate a unique folder name (you can modify this logic as needed)
            folder_name = simpledialog.askstring("Folder Name", "Enter the name of the new folder:")
            folder_count = 1
            while os.path.exists(os.path.join(folder_location, folder_name)):
                folder_name = f"NewFolder_{folder_count}"
                folder_count += 1

            # Create the new folder
            new_folder_path = os.path.join(folder_location, folder_name)
            os.mkdir(new_folder_path)
            self.textbox.insert("1.0", f"Created folder: {new_folder_path}\n")

        else:
            self.textbox.insert("1.0", "Directory location does not exist.\n")

if __name__ == "__main__":
    MyGui()
