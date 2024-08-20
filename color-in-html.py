import cv2
import time

density = 'N@#W$9876543210?!abc;:+=-,._ '
def gbr_to_hex(rgb_array):
    b, g, r = rgb_array
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_color


def html_setup(font, size):
    with open("index.html", "w") as file:
        file.write("<!DOCTYPE html><html><head>")
        file.write("<style>p.small {line-height: 0.8;}</style>")
        file.write("</head><body><p style='font-family: {0}' 'font-size={1}px' class='small'>".format(font, size))

def html_close():
    with open("index.html", "a") as file:
        file.write("</p></body></html>")
    print("HTML file successfully written.")


def color_ascii(img, scale):
    start = time.perf_counter()
    image = cv2.imread(img)
    resize = cv2.resize(image, (0, 0), fx=scale, fy=scale)
    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

    html_setup("Courier New", 10)

    with open("index.html", "a") as file:
        for i in range(resize.shape[0]):
            for j in range(resize.shape[1]):
                value = gray[i, j]
                color = resize[i, j]
                hex_color = gbr_to_hex(color)
                char = density[value // 29]
                file.write(f"<span style='color: {hex_color};'>{char}</span>")
            file.write("<br>")

    html_close()
    end = time.perf_counter()
    print("Time elapsed:{0}".format(end - start))

color_ascii("us!.jpeg", 1)


