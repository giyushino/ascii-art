import cv2
import tkinter as tk
from tkinter import font
import time

density = 'Ñ@#W$9876543210?!abc;:+=-,._ '


def rgb_to_hex(rgb_array):
    b, g, r = rgb_array
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_color


def color_ascii(img, scale):
    start = time.perf_counter()
    values = []
    hexes = []

    image = cv2.imread(img)
    resize = cv2.resize(image, (0, 0), fx=scale, fy=scale)
    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

    for i in range(resize.shape[0]):
        row = []
        hex_row = []
        for j in range(resize.shape[1]):
            value = gray[i, j]
            color = resize[i, j]
            hex_color = rgb_to_hex(color)
            char = density[value // 29]
            row.append(char)
            hex_row.append(hex_color)
        values.append(row)
        hexes.append(hex_row)

    ascii_art = "\n".join("".join(line) for line in values)

    root = tk.Tk()
    root.title("ASCII Art")

    font_name = "Courier"
    font_size = 6
    text_font = font.Font(family=font_name, size=font_size)

    text_widget = tk.Text(root, font=(font_name, font_size), width=len(values[0]), height=len(values))
    text_widget.pack(expand=True, fill='both')

    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')

    text_widget = tk.Text(frame, font=(font_name, font_size), width=len(values[0]), height=len(values))
    scrollbar = tk.Scrollbar(frame, command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)

    text_widget.pack(side=tk.LEFT, expand=True, fill='both')
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    start_index = "1.0"
    for row_idx, (line, hex_row) in enumerate(zip(values, hexes)):
        for col_idx, (char, color) in enumerate(zip(line, hex_row)):
            end_index = f"{row_idx + 1}.{col_idx + 1}"
            text_widget.insert(tk.END, char, (row_idx, col_idx))
            text_widget.tag_add(f"{row_idx}-{col_idx}", start_index, end_index)
            text_widget.tag_configure(f"{row_idx}-{col_idx}", foreground=color)
            start_index = end_index

        text_widget.insert(tk.END, '\n')
        start_index = text_widget.index(tk.END)

    text_widget.config(state=tk.DISABLED)

    root.update_idletasks()
    root.mainloop()
    end = time.perf_counter()
    print(end - start)

color_ascii("us-testing.jpg", 0.5)

