import cv2
import tkinter as tk

density = 'Ñ@#W$9876543210?!abc;:+=-,._ ' #29 characters

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

    # Set the width and height of the window based on the size of the ASCII art
    text_widget = tk.Text(root, font=("Courier", 8), width=len(draw[0]), height=len(draw))
    text_widget.insert(tk.END, ascii_art)
    text_widget.config(state=tk.DISABLED)  # Make the Text widget read-only
    text_widget.pack()
    root.mainloop()


ascii("pia 6.jpg", 0.1)





