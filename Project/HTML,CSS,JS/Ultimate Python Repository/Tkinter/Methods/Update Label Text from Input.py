### Update Label Text from Input ###

import tkinter as tk

def update_label():
    # Retrieve text from the single-line Entry widget
    user_text = entry.get()
    # Update the Label widget with the retrieved text
    result_label.config(text=f"You typed: {user_text}")

root = tk.Tk()
root.title("Get Text from Entry")
root.geometry("400x200")

# Create a single-line input field
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.insert(0, "Type something...")
entry.pack(pady=10)

# Create a button to trigger the action
button = tk.Button(root, text="Submit", command=update_label)
button.pack(pady=5)

# Create a label to display the output result
result_label = tk.DataFrame
result_label = tk.Label(root, text="Your text will appear here", font=("Arial", 12, "bold"))
result_label.pack(pady=20)

root.mainloop()