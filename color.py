import tkinter as tk
from tkinter.colorchooser import askcolor

# Function to open color picker and add color to the palette
def pick_color():
    color = askcolor()[1]  # Open color picker and get selected color (hex)
    if color:  # Check if color is selected (not canceled)
        color_display(color)  # Display the color in the palette

# Function to display the selected color in the palette
def color_display(color):
    palette_frame = tk.Frame(root)
    palette_frame.pack(pady=5)

    color_box = tk.Label(palette_frame, bg=color, width=20, height=2)
    color_box.pack(side="left", padx=5)

    # Add the selected color to the color palette
    color_label = tk.Label(palette_frame, text=color, width=10)
    color_label.pack(side="left", padx=5)

# Setup main window
root = tk.Tk()
root.title("Color Picker with Palette Generator")

# Button to trigger color picker
pick_button = tk.Button(root, text="Pick Color", command=pick_color, height=2, width=20)
pick_button.pack(pady=20)

root.mainloop()
