import cv2
import tkinter as tk
from tkinter import Scrollbar

density = 'Ñ@#W$9876543210?!abc;:+=-,._ '

def ascii(img, scale):
    values = []
    draw = []
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(f"Error: Unable to open image file '{img}'.")
        return

    resize = cv2.resize(image, (0, 0), fx=scale, fy=scale)
    scaling = image.shape[1] / image.shape[0]
    for i in range(0, resize.shape[0]):
        row = []
        for j in range(0, resize.shape[1]):
            value = resize[i, j]
            row.append(value)
        values.append(row)
    for row in values:
        line = []
        for i in row:
            char = density[i//29]
            line.append(char)
        draw.append(line)

    ascii_art = "\n".join("".join(line) for line in draw)

    # Create a new Tkinter window to display the ASCII art
    root = tk.Tk()
    root.title("ASCII Art")

    # Create a frame to contain the text widget and scrollbars
    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)

    # Create the text widget
    text_widget = tk.Text(frame, font=("Courier", 8), wrap='none')
    text_widget.insert(tk.END, ascii_art)
    text_widget.config(state=tk.DISABLED)  # Make the Text widget read-only

    # Create vertical and horizontal scrollbars
    v_scroll = Scrollbar(frame, orient='vertical', command=text_widget.yview)
    h_scroll = Scrollbar(frame, orient='horizontal', command=text_widget.xview)

    # Configure the text widget to use the scrollbars
    text_widget.config(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

    # Pack the scrollbars and text widget
    v_scroll.pack(side='right', fill='y')
    h_scroll.pack(side='bottom', fill='x')
    text_widget.pack(side='left', fill='both', expand=True)

    root.mainloop()


ascii("pia 6.jpg", 0.1)
