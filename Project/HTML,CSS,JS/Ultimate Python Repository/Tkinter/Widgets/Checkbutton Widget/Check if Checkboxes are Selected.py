### Check if Checkboxes are Selected and Display Output ###

import tkinter as tk

def show_selection():
    # .get() returns 1 if checked, 0 if unchecked
    selection = []
    if var1.get() == 1:
        selection.append("Option 1")
    if var2.get() == 1:
        selection.append("Option 2")
    
    # Update the label text
    if selection:
        label.config(text=f"Selected: {', '.join(selection)}")
    else:
        label.config(text="No options selected")

root = tk.Tk()
root.title("Checkbox Widget - Check Box")
root.geometry("600x400")

# Define variables to hold the checkbox states (0 or 1)
var1 = tk.IntVar()
var2 = tk.IntVar()

# Create Checkbutton widgets
cb1 = tk.Checkbutton(root, text="Option 1", variable=var1, command=show_selection)
cb1.pack(pady=10)

cb2 = tk.Checkbutton(root, text="Option 2", variable=var2, command=show_selection)
cb2.pack(pady=10)

# Create a label to display the output
label = tk.Label(root, text="No options selected")
label.pack(pady=20)

root.mainloop()