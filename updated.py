import cv2
import tkinter as tk
from tkinter import font

density = 'Ñ@#W$9876543210?!abc;:+=-,._ '  # 29 characters

def ascii(img, scale):
    values = []
    draw = []
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(f"Error: Unable to open image file '{img}'.")
        return

    resize = cv2.resize(image, (0, 0), fx=scale, fy=scale)
    for i in range(0, resize.shape[0]):
        row = []
        for j in range(0, resize.shape[1]):
            value = resize[i, j]
            row.append(value)
        values.append(row)
    for row in values:
        line = []
        for i in row:
            char = density[i // 29]
            line.append(char)
        draw.append("".join(line))

    root = tk.Tk()
    root.title("ASCII Art")

 
    font_name = "Courier"
    font_size = 6
    text_font = font.Font(family=font_name, size=font_size)


    char_width = text_font.measure('M')  
    char_height = text_font.metrics('linespace')  

    text_width = max(text_font.measure(line) for line in draw)
    text_height = len(draw) * char_height

    canvas_frame = tk.Frame(root)
    canvas_frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(canvas_frame, bg='white', width=text_width, height=text_height)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    v_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=canvas.yview)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    h_scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=canvas.xview)
    h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    canvas.config(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    text_id = canvas.create_text(0, 0, anchor="nw", text="\n".join(draw), font=text_font, width=text_width)

  
    canvas.update_idletasks()  
    bbox = canvas.bbox(text_id)
    canvas.config(scrollregion=bbox)

  
    def on_mouse_wheel(event):
        if event.state & 0x0001:  =
            canvas.xview_scroll(int(-1*(event.delta/120)), "units")
        else:
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

    root.mainloop()

ascii("us!.jpeg", 0.1)
